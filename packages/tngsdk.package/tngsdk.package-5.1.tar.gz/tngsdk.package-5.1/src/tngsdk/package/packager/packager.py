#  Copyright (c) 2018 SONATA-NFV, 5GTANGO, UBIWHERE, Paderborn University
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV, 5GTANGO, UBIWHERE, Paderborn University
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).
#
# This work has also been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).
import os
import threading
import uuid
import time
import io
import yaml
import re
import datetime
import pprint
import pyrfc3339
import hashlib
import tempfile
from tngsdk.package.helper import dictionary_deep_merge, file_hash,\
    search_for_file, creat_zip_file_from_directory
from tngsdk.package.logger import TangoLogger
from tngsdk.package.validator import validate_project_with_external_validator
from tngsdk.package.packager.exeptions import MissingInputException,\
    MissingMetadataException, MissingFileException, ChecksumException,\
    MetadataValidationException
from distutils.version import LooseVersion


LOG = TangoLogger.getLogger(__name__)


DESCRIPTOR_MIME_TYPES = ["application/vnd.5gtango.nsd",
                         "application/vnd.5gtango.vnfd",
                         "application/vnd.5gtango.tstd"]


class PkgStatus(object):
    WAITING = "waiting"
    RUNNING = "running"
    FAILED = "failed"
    SUCCESS = "success"


class NapdRecord(object):
    """
    This class represents a runtime version
    of the NFV advanced package descriptor.
    It is the unified data model on which the
    package works.
    It is generated from the original NAPD
    YAML format but contains additional metadata,
    namely pointers to raw TOSCA or ETSI metadata.
    nr.metadata["tosca"] = [block0, block1 ...]
    """
    def __init__(self, **kwargs):
        self.error = None
        self.warning = None
        self.descriptor_schema = ("https://raw.githubusercontent.com"
                                  + "/sonata-nfv/tng-schema/master/"
                                  + "package-specification/napd-schema.yml")
        self.vendor = None
        self.name = None
        self.version = None
        self.package_type = None
        self.maintainer = None
        self.release_date_time = None
        self.metadata = dict()
        self.package_content = list()
        self.description = None
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "NapdRecord({})".format(pprint.pformat(self.to_dict()))

    def find_package_content_entry(self, source):
        for ce in self.package_content:
            if ce.get("source") == source:
                return ce
        return None

    def to_dict(self):
        return self.__dict__.copy()

    def to_clean_dict(self):
        """
        Return a cleaned-up version of the dict.
        """
        d = self.to_dict()
        # root
        if "error" in d:
            del d["error"]
        if "warning" in d:
            del d["warning"]
        if "metadata" in d:
            del d["metadata"]
        if "_project_wd" in d:
            del d["_project_wd"]
        # package content
        for pc in d.get("package_content"):
            if "_project_source" in pc:
                del pc["_project_source"]
        return d

    @property
    def pkg_id(self):
        pass  # TODO

    def update(self, data_dict):
        """
        Overwrites the values of this record
        using the values from the given dict.
        """
        # deep merge
        dictionary_deep_merge(
            self.__dict__, data_dict, skip=["package_content"])
        # deep merge individual items of package_content (if available)
        if "package_content" in data_dict:
            for ce in data_dict.get("package_content"):
                if ("source" not in ce
                        or "algorithm" not in ce
                        or "hash" not in ce):
                    continue  # skip incomplete entries
                existing_ce = (
                    self.find_package_content_entry(ce.get("source")))
                if existing_ce is not None:
                    dictionary_deep_merge(existing_ce, ce)
                else:  # additional entry
                    self.package_content.append(ce)


class Packager(object):
    """
    Abstract packager class.
    Takes care about asynchronous packaging processes.
    Actual packaging/unpackaging methods have to be overwritten
    by format-specific packager classes.
    """

    def __init__(self, args, storage_backend=None):
        # unique identifier for this package request
        self.uuid = uuid.uuid4()
        self.status = PkgStatus.WAITING
        self.storage_backend = storage_backend
        self.error_msg = None
        self.args = args
        self.result = NapdRecord()
        self.version_incremented = False
        self.checksum_algorithm = "SHA-256"
        LOG.info("Packager created: {}".format(self),
                 extra={"start_stop": "START"})
        LOG.debug("Packager args: {}".format(self.args))
        if (self.storage_backend is None
                and self.args.unpackage is not None):
            LOG.warning("Disabled storage backend: store_skip=True?")

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.uuid)

    def _wait_for_thread(self, t):
        while t.is_alive():
            LOG.debug("Waiting for package/unpackage process ...")
            # TODO display a nicer process status when in CLI mode
            t.join(timeout=0.5)

    def package(self, callback_func=None):
        t = threading.Thread(
            target=self._thread_package,
            args=(callback_func,))
        t.daemon = True
        self.status = PkgStatus.RUNNING
        t.start()
        if callback_func is None:
            # behave synchronous if callback is None
            self._wait_for_thread(t)

    def unpackage(self, callback_func=None):
        t = threading.Thread(
            target=self._thread_unpackage,
            args=(callback_func,))
        t.daemon = True
        self.status = PkgStatus.RUNNING
        t.start()
        if callback_func is None:
            # behave synchronous if callback is None
            self._wait_for_thread(t)

    def _thread_unpackage(self, callback_func):
        t_start = time.time()
        # call format specific implementation
        self.result = self._do_unpackage()
        LOG.info("Packager done ({:.4f}s): {} error: {}".format(
            time.time()-t_start, self, self.result.error),
            extra={"start_stop": "STOP",
                   "time_elapsed": str(time.time()-t_start)})
        if self.result.error is None:
            self.status = PkgStatus.SUCCESS
        else:
            self.status = PkgStatus.FAILED
        # callback
        if callback_func:
            callback_func(self)

    def _thread_package(self, callback_func):
        t_start = time.time()
        # call format specific implementation
        self.result = self._do_package()
        LOG.info("Packager done ({:.4f}s): {}".format(
            time.time()-t_start, self),
            extra={"start_stop": "STOP",
                   "time_elapsed": str(time.time()-t_start)})
        self.status = PkgStatus.SUCCESS
        # callback
        if callback_func:
            callback_func(self)

    def _do_unpackage(self, *args, **kwargs):
        LOG.error("_do_unpackage has to be overwritten")
        # time.sleep(2)
        return NapdRecord(error="_do_unpackage has to be overwritten")

    def _do_package(self, *args, **kwargs):
        LOG.error("_do_package has to be overwritten")
        # time.sleep(2)
        return NapdRecord(error="_do_package has to be overwritten")

    @staticmethod
    def _do_package_closure(function):
        def _do_package_function(self):
            if self.args is not None:
                project_path = self.args.package
            else:
                LOG.error("No project path. Abort.")
                return NapdRecord()
            LOG.info("Creating 5GTANGO package using project: '{}'"
                     .format(project_path))
            try:
                # 0. validate project with external validator
                if (self.args.skip_validation or
                        self.args.validation_level == "skip" or
                        os.environ.get("SKIP_VALIDATION", "False") == "True"):
                    LOG.warning(
                        "Skipping validation (--skip-validation).")
                else:
                    validate_project_with_external_validator(
                        self.args, project_path)
                # 1. find and load project descriptor
                if project_path is None or project_path == "None":
                    raise MissingInputException("No project path. Abort.")
                project_descriptor = self._pack_read_project_descriptor(
                    project_path)
                if project_descriptor is None:
                    raise MissingMetadataException(
                        "No project descriptor found.")
                if self.args.autoversion:
                    project_descriptor = self.autoversion(project_descriptor)
                if not self.args.no_subfolder_compression:
                    self.compress_subfolders(project_descriptor,
                                             project_path)
                else:
                    LOG.warning("Ignoring subfolder because of argument" +
                                " --no-subfolder-compression")
                    _type = 'application/vnd.folder.compressed.zip'

                    def _filter(file):
                        return file["type"] != _type

                    project_descriptor["files"] = \
                        list(filter(_filter, project_descriptor["files"]))
                # 2. create a NAPDR for the new package
                napdr = self._pack_create_napdr(project_path,
                                                project_descriptor)
                napdr.package_type = self._pack_get_package_type(napdr)
                LOG.debug("Generated NAPDR: {}".format(napdr))
                # 3. create a temporary working directory
                napdr._project_wd = tempfile.mkdtemp()
                LOG.debug("Created temp. working directory: {}"
                          .format(napdr._project_wd))

                napdr = function(**locals())

                self.store_autoversion(project_descriptor, project_path)
                return napdr
            except BaseException as e:
                LOG.error("{}; Exception of type: {}".format(
                    str(e), str(type(e))))
                self.error_msg = str(e)
                return NapdRecord(error=str(e))

        return _do_package_function

    def compress_subfolders(self, project_descriptor, pp):
        """
        Finds subfolders (package_content of type
        'application/vnd.folder.compressed.zip') and zips them to a temp
        directory.
        Args:
            project_descriptor:
            pp:

        Returns:
            None
        """
        for file in project_descriptor["files"]:
            if 'application/vnd.folder.compressed.zip' == file["type"]:
                file["_project_source"] = self.zip_subfolder(pp=pp, **file)

    def zip_subfolder(self, path, pp, **kwargs):
        """
        Zipping folder at path to a temporary directory.
        Args:
            path:
            pp:
            **kwargs:

        Returns:
            path to the zip file
        """
        tmp = tempfile.mkdtemp()
        filename = "{}.zip".format(os.path.basename(path))
        src = os.path.join(pp, path)
        dest = os.path.join(tmp, filename)
        creat_zip_file_from_directory(src, dest)
        return dest

    def _pack_get_package_type(self, napdr):
        """
        Guess package type based on contents.
        if NSD exists -> application/vnd.5gtango.package.nsp
        if VNF exists -> application/vnd.5gtango.package.vnfp
        if TSTD exists -> application/vnd.5gtango.package.tdp
        else -> error
        """
        types = [pc.get("content-type") for pc in napdr.package_content]
        if "application/vnd.5gtango.nsd" in types:
            return "application/vnd.5gtango.package.nsp"
        if "application/vnd.etsi.osm.nsd" in types:
            return "application/vnd.5gtango.package.nsp"
        if "application/vnd.lf.onap.nsd" in types:
            return "application/vnd.5gtango.package.nsp"
        if "application/vnd.5gtango.vnfd" in types:
            return "application/vnd.5gtango.package.vnfp"
        if "application/vnd.etsi.osm.vnfd" in types:
            return "application/vnd.5gtango.package.vnfp"
        if "application/vnd.lf.onap.vnfd" in types:
            return "application/vnd.5gtango.package.vnfp"
        if "application/vnd.5gtango.tstd" in types:
            return "application/vnd.5gtango.package.tdp"
        raise BaseException("Could not detect package type!"
                            + " No NSD, VNFD or TSTD found.")

    def _pack_read_project_descriptor(self, project_path):
        """
        Searches and reads, validates project.y*l for packaging.
        """
        # find file
        project_descriptor_path = search_for_file(
            path=os.path.join(project_path, "project.y*l"))
        if project_descriptor_path is None:
            raise MissingFileException(
                "project.y*l not found in {}".format(project_path))
        # read file
        with open(project_descriptor_path, "r") as f:
            data = yaml.load(f)
            # validate contents
            for field in ["package", "files", "version"]:
                if field not in data:
                    raise MetadataValidationException(
                        "{} section missing in PD".format(field))
            for field in ["name", "vendor", "version"]:
                if field not in data["package"]:
                    raise MetadataValidationException(
                        "{} field missing in PD/package".format(field))
            # check if all linked files exist
            for f in data.get("files"):
                if (f.get("path") is None or
                    not os.path.isfile(
                        os.path.join(project_path, f.get("path"))) and
                    not f.get("type") ==
                        "application/vnd.folder.compressed.zip"):
                    raise MissingFileException(
                        "Could not find file linked in project.yml:{}".format(
                            f.get("path")))
            return data
        return None

    def _pack_create_napdr(self, pp, pd):
        """
        Creates a NAPDR for the new package based on the given
        project path (pp) and project descriptor (pd).

        NAPDR is annotated with info. like '_project_source' to
        temp. link between project files and target package.
        """
        # create initial NAPDR with package contents of project (name etc.)
        napdr = NapdRecord(**pd.get("package"))
        # add release date and time
        napdr.release_date_time = pyrfc3339.generate(
            datetime.datetime.now(), accept_naive=True)
        # add package content
        for f in pd.get("files"):
            r = {"source": self._pack_package_source_path(f),
                 "algorithm": self.checksum_algorithm,
                 "hash": self.file_hash(
                     os.path.join(pp, self._project_source_path(f))),
                 "content-type": f.get("type", "text/plain"),
                 "tags": f.get("tags"),
                 "testing_tags": f.get("testing_tags"),
                 "_project_source": self._project_source_path(f),
                 }
            # turn tag fields that are "None" into empty lists
            if r.get("tags") is None:
                r["tags"] = list()
            if r.get("testing_tags") is None:
                r["testing_tags"] = list()
            napdr.package_content.append(r)
        return napdr

    def file_hash(self, *args, **kwargs):
        return file_hash(*args, **kwargs)

    def _pack_package_source_path(self, f):
        """
        Returns the path of the given file in the
        generated package.
        We need to translate here, because known
        descriptor formats are moved to the Definitions/ folder
        to be TOSCA compatible.
        """
        if f.get("type") in DESCRIPTOR_MIME_TYPES:
            # translate
            return os.path.join("Definitions/", f.get("path"))
        # use original
        if f.get("type") == 'application/vnd.folder.compressed.zip':
            return "{}.zip".format(f.get("path"))
        return f.get("path")

    def _project_source_path(self, f):
        if "_project_source" in f:
            return f["_project_source"]
        else:
            return f.get("path")

    def autoversion(self, project_descriptor, index=2):
        """
        Increases project_descriptor["package"]["version"], on digit,
        specified by index. Returns new project_descriptor. If succeful,
        self.version_incremented is set to True (for store_autoversion()).
        Used in TangoPackager._do_package().
        """
        project_descriptor = project_descriptor.copy()
        project_descriptor["package"] = project_descriptor["package"].copy()
        version = project_descriptor["package"]["version"]
        try:
            version = LooseVersionExtended(version)
            version.increment(index)

            project_descriptor["package"]["version"] = str(version)
            self.version_incremented = True
        except Exception as e:
            LOG.warning("Autoversion failed: {}, {}".format(type(e), e))
            self.version_incremented = False
        return project_descriptor

    def store_autoversion(self, project_descriptor, project_descriptor_path,
                          project_descriptor_filename="project.yml"):
        """
        Stores given project_descriptor to project_descriptor_path, if
        self.version_incremented is True.
        """
        if not self.version_incremented:
            return False
        try:
            with open(os.path.join(project_descriptor_path,
                                   project_descriptor_filename), "w") as f:
                yaml.dump(project_descriptor, f, default_flow_style=False)
        except Exception as e:
            LOG.warning("""Store autoversion failed,
                but package of new version created: {}, {}""".format(
                                                type(e), e))
            return False
        return True


class TestPackager(Packager):

    def _do_unpackage(self):
        return NapdRecord()

    def _do_package(self):
        return NapdRecord()


class CsarBasePackager(Packager):

    def collect_metadata(self, wd):
        LOG.debug("Collecting TOSCA CSAR meta data ...")
        return self._update_nr_with_tosca(
            self._read_tosca_meta(wd))

    def _update_nr_with_tosca(self, tosca_meta, nr=None):
        """
        Creates a NapdRecord and fills it with TOSCA
        meta data. Mapping/translation is done manually since many
        required fields are not in TOSCA.
        """
        if nr is None:
            nr = NapdRecord()
        # TOSCA Created-By becomes vendor
        nr.vendor = save_name(tosca_meta[0].get("Created-By"))
        # TOSCA has no name field: Use UUID of process instead
        nr.name = str(uuid.uuid4())[:8]
        # TOSCA has no package version. Use 1.0
        nr.version = "1.0"
        # Package type = application/vnd.tosca.package
        nr.package_type = "application/vnd.tosca.package"
        # Maintainer = Created By
        nr.maintainer = tosca_meta[0].get("Created-By")
        # TOSCA has no create date/time: Use current time
        nr.release_date_time = pyrfc3339.generate(
            datetime.datetime.now(), accept_naive=True)
        # add raw TOSCA metadata
        nr.metadata["tosca"] = tosca_meta
        # LOG.debug("Added TOSCA meta data to {}".format(nr))
        return nr

    def _read_tosca_meta(self, wd):
        """
        Tries to find TOSCA.meta file.
        Returns list of blocks from that file
        or an list with a single empty block.
        """
        try:
            path = search_for_file(os.path.join(wd, "**/TOSCA.meta"))
            if path is None:
                raise MissingMetadataException("Cannot find TOSCA.meta")
            with open(path, "r") as f:
                return parse_block_based_meta_file(f)
        except BaseException as e:
            LOG.error("Cannot read TOSCA metadata: {}".format(e))
        return [{}]


class EtsiPackager(CsarBasePackager):

    def collect_metadata(self, wd):
        nr = super().collect_metadata(wd)
        LOG.debug("Collecting ETSI manifest meta data ...")
        etsi_mf = self._read_etsi_manifest(
            wd, nr.metadata.get("tosca"))
        # update nr with ETSI info
        return self._update_nr_with_etsi(etsi_mf, nr)

    def _update_nr_with_etsi(self, etsi_mf, nr=None):
        """
        Updates NR with data from ETSI manifest input.
        """
        if nr is None:
            nr = NapdRecord()
        # find package_type
        if len(etsi_mf[0]) > 0:
            nr.package_type = self._etsi_to_napd_package_type(etsi_mf)
        # select ETSI key prefix based on pkg.type
        prefix = "vnf"
        if nr.package_type == "application/vnd.etsi.package.nsp":
            prefix = "ns"
        elif nr.package_type == "application/vnd.etsi.package.tdp":
            prefix = "test"
        # vendor, name, version = provider_id, product_name, package_version
        nr.vendor = etsi_mf[0].get("{}_provider_id".format(prefix), nr.vendor)
        nr.name = etsi_mf[0].get("{}_product_name".format(prefix), nr.name)
        nr.version = etsi_mf[0].get(
            "{}_package_version".format(prefix), nr.version)
        # only overwrite maintainer if not set by TOSCA.meta
        if nr.maintainer is None:
            nr.maintainer = etsi_mf[0].get("{}_provider_id".format(prefix))
        # release_date_time = release_date_time
        nr.release_date_time = etsi_mf[0].get(
            "{}_release_date_time".format(prefix), nr.release_date_time)
        # add package_content based on ETSI manifest blocks 1...n
        nr.package_content = self._etsi_to_napd_package_content(etsi_mf)
        # add raw ETSI manifest
        nr.metadata["etsi"] = etsi_mf
        # LOG.debug("Added ETSI meta data to {}".format(nr))
        return nr

    def _etsi_to_napd_package_content(self, etsi_mf):
        """
        Translates block1 to blockN of ETSI MF to
        NAPD-like package_content entries.
        """
        if len(etsi_mf) < 2:
            return list()
        result = list()
        for i in range(1, len(etsi_mf)):
            # translate block1 to blockN
            block = etsi_mf[i]
            if "Source" not in block or block.get("Source") is None:
                LOG.warning("Skipping block in ETSI MF: {}".format(block))
                continue
            pc = {"source": block.get("Source"),
                  "algorithm": block.get("Algorithm"),
                  "hash": block.get("Hash"),
                  "content-type": None}  # TODO guess MIME type here
            result.append(pc)
        return result

    def _etsi_to_napd_package_type(self, etsi_mf):
        """
        Find package_type based on key names of block0.
        """
        for k, _ in etsi_mf[0].items():
            if "ns_" in k:
                return "application/vnd.etsi.package.nsp"
            elif "test_" in k:
                return "application/vnd.etsi.package.tdp"
        # default: assume VNF package
        return "application/vnd.etsi.package.vnfp"

    def _read_etsi_manifest(self, wd, tosca_meta):
        """
        Tries to find ETSI Manifest file.
        - try 1: Use "Entry-Manifest" from TOSCA.meta
        - try 2: Look for *.mf file in root of package
        Returns list of blocks from that file
        or an empty list.
        """
        try:
            if (tosca_meta is not None
                    and tosca_meta[0].get("Entry-Manifest") is not None):
                # try 1:
                path = search_for_file(
                    os.path.join(wd, tosca_meta[0].get("Entry-Manifest")))
                if path is None:
                    LOG.warning("Entry-Manifest '{}' not found.".format(
                        tosca_meta[0].get("Entry-Manifest")))
                    # try 2:
                    path = search_for_file(
                        os.path.join(wd, "*.mf"), recursive=False)
            if path is None:
                raise MissingMetadataException(
                    "Cannot find ETSI manifest file.")
            with open(path, "r") as f:
                return parse_block_based_meta_file(f)
        except BaseException as e:
            LOG.error("Cannot read ETSI manifest file: {}".format(e))
        return [{}]

    def _validate_package_content_checksums(self, wd, napdr):
        """
        Validates the checksums of all entries in the
        package_content list.
        (if algorithm field is not given, nothing is checked)
        Implemented on the ETSI level, because CSAR packages do
        not have checksums to check.
        """
        # iterate over all content files and check them
        for ce in napdr.package_content:
            # check and validate ce data
            if "source" not in ce:
                raise MissingMetadataException(
                    """Malformed package_content entry:
                    source field missing: {}"""
                    .format(ce))
            if ce.get("algorithm") is None:
                # warn and skip entry (a risk but makes things easier for now)
                LOG.warning("Package content without checksum: {}".format(ce))
                continue
            if ce.get("algorithm") is not None and ce.get("hash") is None:
                raise ChecksumException("Checksum missing: {}"
                                        .format(ce))
            # find file
            path = search_for_file(os.path.join(wd, ce.get("source")))
            if path is None:
                raise MissingFileException(
                    "Checksum: File not found: {}".format(
                        os.path.join(wd, ce.get("source"))))
            # validate checksum
            try:
                validate_file_checksum(
                    path, ce.get("algorithm"), ce.get("hash"))
            except ChecksumException as e:
                # decide if checksum missmatch is error
                print(self.args.no_checksums)
                if self.args.no_checksums:
                    # LOG.warning(e)
                    LOG.warning("Ignoring error (--ignore-checksums)")
                else:
                    raise e


# #########################
# Helpers
# #########################


def parse_block_based_meta_file(inputs):
    """
    Parses a block-based meta data file, like used by TOSCA.
    Return list of dicts. Each dict is a block.
    param: inputs: string or file IO object
    [block1, block2, blockN]
    """
    def _parse_line(l):
        prts = l.split(":")  # colon followed by space (TOSCA)
        if len(prts) < 2:
            LOG.warning("Malformed line in block: '{}' len: {}"
                        .format(l, len(l)))
            return None, None
        key = str(prts.pop(0)).strip()  # first part is keys
        value = (":".join(prts)).strip()  # rest is value
        return key, value

    blocks = list()
    # extract content as stirng
    content = ""
    if isinstance(inputs, io.IOBase):
        # read content from file
        content = inputs.read()
    else:  # assume string as input
        content = inputs
    # parse line by line and build blocks
    curr_block = dict()
    for l in content.split("\n"):
        if len(l.strip()) < 1:
            # new block (empty line)
            if len(curr_block) > 0:
                blocks.append(curr_block.copy())
            curr_block = dict()
        else:  # parse line and add to curr_block
            k, v = _parse_line(l.strip())
            if k is not None:
                curr_block[k] = v
    if len(blocks) < 1:
        # ensure that block_0 is always there
        LOG.warning("No blocks found in: {}".format(inputs))
        blocks.append(dict())
    return blocks


def save_name(s):
    """
    Turns any string into a string
    without spaces.
    """
    if s is None:
        return None
    s = re.sub(r"[^A-Za-z0-9 ]", "", s)
    return s.replace(" ", "-")


def validate_file_checksum(path, algorithm, hash_str):
    """
    Validate checksum of given file.
    Raises ChecksumException
    """
    supported_algorithms = ["SHA-256", "SHA-1", "MD5"]
    if algorithm not in supported_algorithms:
        raise ChecksumException("Unsupported algorithm: {}"
                                .format(algorithm))
    if hash_str is None or len(hash_str) < 1:
        raise ChecksumException("Cannot validate empty hash: {}"
                                .format(hash_str))
    # select hash function
    h_func = hashlib.md5  # default
    if algorithm == "SHA-256":
        h_func = hashlib.sha256
    if algorithm == "SHA-1":
        h_func = hashlib.sha1
    # check if file exists
    if path is None or not os.path.isfile(path):
        raise ChecksumException("Checksum: File not found: {}"
                                .format(path))
    # try to compute the files checksum
    try:
        h_file = file_hash(path, h_func)
    except BaseException as e:
        msg = "Coudn't compute file hash {}".format(path)
        LOG.exeception(msg)
        del e
        raise ChecksumException(msg)
    # compare checksums
    if h_file != hash_str:
        msg = "Checksum mismatch! {}({}) != napdr({})".format(
            path, h_file, hash_str)
        LOG.error(msg)
        raise ChecksumException(msg)


class LooseVersionExtended(LooseVersion):
    """
    Parsing helper for Packager.autoversion.
    Docstrings and source code of super class:
    https://hg.python.org/cpython/file/tip/Lib/distutils/version.py
    """
    def __init__(self, vstring, *args, **kwargs):
        super().__init__(str(vstring), *args, **kwargs)

    def increment(self, index=-1, to=1):
        if index > len(self.version)-1:
            self.version.extend([0]*(index+1-len(self.version)))
        self.version[index] += to
        self.vstring = self.__str__()

    def __str__(self):
        return ".".join(list(map(str, self.version)))

    def parse(self, *args, **kwargs):
        super().parse(*args, **kwargs)
        self.version = list(map(int, self.version))
