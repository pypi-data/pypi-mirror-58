#  Copyright (c) 2015 SONATA-NFV, 5GTANGO, UBIWHERE, Paderborn University
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


import unittest
import threading
import yaml
import os
import zipfile
from tngsdk.package.cli import parse_args
from tngsdk.package.packager import PM
from tngsdk.package.packager.packager import parse_block_based_meta_file
from tempfile import NamedTemporaryFile, mkdtemp


class TngSdkPackagePackagerHelperTest(unittest.TestCase):

    def setUp(self):
        # list can manually define CLI arguments
        self.default_args = parse_args([])

    def tearDown(self):
        pass

    # @unittest.skip("skip")
    def test_parse_block_based_meta_file(self):
        # test case
        i = """
            Key1: Value1
            """
        b = parse_block_based_meta_file(i)
        self.assertEqual(len(b), 1)
        # test case
        i = """
            Key1: Value1
            Key2: Value2: Value
            """
        b = parse_block_based_meta_file(i)
        self.assertEqual(len(b), 1)
        self.assertEqual(b[0], {"Key1": "Value1", "Key2": "Value2: Value"})
        # test case
        i = """

            Key1: Value1
            Key1: Value1
            Key1: Value1

            Key1: Value1

            Key1: Value1

            Key1: Value1
            """
        b = parse_block_based_meta_file(i)
        self.assertEqual(len(b), 4)


class TngSdkPackagePackagerTest(unittest.TestCase):

    def setUp(self):
        # list can manually define CLI arguments
        self.default_args = parse_args([])

    def tearDown(self):
        pass

    def test_instantiation_default(self):
        p = PM.new_packager(self.default_args)
        self.assertIn("TangoPackager", str(type(p)))
        del p

    def test_instantiation_tango(self):
        p = PM.new_packager(self.default_args, pkg_format="eu.5gtango")
        self.assertIn("TangoPackager", str(type(p)))
        del p

    def test_instantiation_etsi(self):
        p = PM.new_packager(self.default_args, pkg_format="eu.etsi")
        self.assertIn("EtsiPackager", str(type(p)))
        del p

    def test_package_sync(self):
        p = PM.new_packager(self.default_args, pkg_format="test")
        p.package()

    def test_unpackage_sync(self):
        p = PM.new_packager(self.default_args, pkg_format="test")
        p.unpackage()

    def test_package_async(self):
        lock = threading.Semaphore()
        lock.acquire()

        def cb(args):
            lock.release()

        p = PM.new_packager(self.default_args, pkg_format="test")
        p.package(callback_func=cb)
        self.assertTrue(lock.acquire(timeout=3.0),
                        msg="callback was not called before timeout")

    def test_unpackage_async(self):
        lock = threading.Semaphore()
        lock.acquire()

        def cb(args):
            lock.release()

        p = PM.new_packager(self.default_args, pkg_format="test")
        p.unpackage(callback_func=cb)
        self.assertTrue(lock.acquire(timeout=3.0),
                        msg="callback was not called before timeout")

    def test_autoversion(self):
        p = PM.new_packager(self.default_args, pkg_format="test")
        project_descriptors = [{"package": {"version": "1.0"}},
                               {"package": {"version": "1.0.3"}},
                               {"package": {"version": 1.5}},
                               {"package": {"version": "1"}},
                               {"package": {"version": 1}},
                               {"package": {"version": "."}}]
        project_descriptor_results = [{"package": {"version": "1.0.1"}},
                                      {"package": {"version": "1.0.4"}},
                                      {"package": {"version": "1.5.1"}},
                                      {"package": {"version": "1.0.1"}},
                                      {"package": {"version": "1.0.1"}},
                                      {"package": {"version": "0.0.1"}}]
        for desc, result in zip(project_descriptors,
                                project_descriptor_results):
            self.assertEqual(p.autoversion(desc), result)  # incremented?
            self.assertTrue(p.version_incremented,
                            msg=str(desc)+", "+str(result))
            # Flag set?

        project_descriptors_invalid = [{"package": {"version": ""}},
                                       {"package": {"version": "text"}}]

        for desc in project_descriptors_invalid:
            project_descriptor = p.autoversion(desc)
            self.assertEqual(project_descriptor, desc)  # no changes if failed
            self.assertFalse(p.version_incremented, msg=str(desc))

    def test_store_autoversion(self):
        # Set up test
        tmp = NamedTemporaryFile()
        project_descriptor_path = ""
        project_descriptor_filename = tmp.name
        test_dict = {"test": "test"}
        f = open(project_descriptor_filename, "w")
        yaml.dump(test_dict, f, default_flow_style=False)
        f.close()

        p = PM.new_packager(self.default_args, pkg_format="test")
        project_descriptor = {"package": {"version": "1.0.1"}}

        # store to fail
        self.assertFalse(p.store_autoversion(project_descriptor,
                                             project_descriptor_path))
        f = open(project_descriptor_filename, "r")
        result = yaml.load(f)
        f.close()
        self.assertEqual(result, test_dict)

        # succeful store
        p.version_incremented = True
        self.assertTrue(p.store_autoversion(project_descriptor,
                                            project_descriptor_path,
                                            project_descriptor_filename))
        f = open(project_descriptor_filename, "r")
        result = yaml.load(f)
        f.close()
        self.assertEqual(result, project_descriptor)

    def test_zip_subfolder(self):
        tmp = mkdtemp()
        tmp_files = [NamedTemporaryFile(dir=tmp) for i in range(5)]
        file_descriptor = {"path": tmp}

        p = PM.new_packager(self.default_args, pkg_format="test")
        dest = p.zip_subfolder(pp=".", **file_descriptor)

        self.assertTrue(os.path.isfile(dest))
        self.assertEqual(os.path.splitext(dest)[1], ".zip")

        with zipfile.ZipFile(dest) as zf:
            names = zf.namelist()
            for file in tmp_files:
                self.assertIn(os.path.basename(file.name), names)

    def test_compress_subfolders(self):
        tmp_subfolders = [mkdtemp() for i in range(5)]
        tmp_files = [[NamedTemporaryFile(dir=tmp) for i in range(5)]
                     for tmp in tmp_subfolders]
        file_descriptors = [{"path": tmp,
                             "type": "application/vnd.folder.compressed.zip"}
                            for tmp in tmp_subfolders]
        file_descriptors_not_subfolder = [{"path": "path/to", "type": "type"}
                                          for i in range(5)]
        project_descriptor = {
            "files": file_descriptors + file_descriptors_not_subfolder}

        p = PM.new_packager(self.default_args, pkg_format="test")
        p.compress_subfolders(project_descriptor, ".")

        for i, file in enumerate(project_descriptor["files"]):
            if file["type"] != "application/vnd.folder.compressed.zip":
                continue
            self.assertTrue(os.path.exists(file["_project_source"]),
                            msg=os.listdir(
                                os.path.dirname(file["_project_source"])))
            self.assertTrue(os.path.isfile(file["_project_source"]),
                            msg=os.listdir(
                                os.path.dirname(file["_project_source"])))
            self.assertEqual(os.path.splitext(file["_project_source"])[1],
                             ".zip")

            with zipfile.ZipFile(file["_project_source"]) as zf:
                names = zf.namelist()
                for tmp_file in tmp_files[i]:
                    self.assertIn(os.path.basename(tmp_file.name), names)
