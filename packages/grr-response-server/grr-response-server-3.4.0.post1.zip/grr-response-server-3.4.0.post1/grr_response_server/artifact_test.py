#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Tests for artifacts."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import io
import logging
import os
import subprocess

from absl import app
from future.builtins import str

import mock

from grr_response_client import actions
from grr_response_client.client_actions import searching
from grr_response_client.client_actions import standard
from grr_response_core import config
from grr_response_core.lib import parser
from grr_response_core.lib import parsers
from grr_response_core.lib import rdfvalue
from grr_response_core.lib import utils
from grr_response_core.lib.parsers import linux_file_parser
from grr_response_core.lib.parsers import wmi_parser
from grr_response_core.lib.rdfvalues import anomaly as rdf_anomaly
from grr_response_core.lib.rdfvalues import artifacts as rdf_artifacts
from grr_response_core.lib.rdfvalues import client as rdf_client
from grr_response_core.lib.rdfvalues import client_fs as rdf_client_fs
from grr_response_core.lib.rdfvalues import paths as rdf_paths
from grr_response_core.lib.rdfvalues import protodict as rdf_protodict
from grr_response_server import action_registry
from grr_response_server import artifact
from grr_response_server import artifact_registry
from grr_response_server import data_store
from grr_response_server import file_store
from grr_response_server import server_stubs
from grr_response_server.databases import db
from grr_response_server.flows.general import collectors
from grr_response_server.flows.general import filesystem
from grr_response_server.rdfvalues import flow_objects as rdf_flow_objects
from grr_response_server.rdfvalues import objects as rdf_objects
from grr.test_lib import action_mocks
from grr.test_lib import artifact_test_lib
from grr.test_lib import client_test_lib
from grr.test_lib import flow_test_lib
from grr.test_lib import parser_test_lib
from grr.test_lib import test_lib
from grr.test_lib import vfs_test_lib

# pylint: mode=test

WMI_SAMPLE = [
    rdf_protodict.Dict({
        u"Version": u"65.61.49216",
        u"InstallDate2": u"",
        u"Name": u"Google Chrome",
        u"Vendor": u"Google, Inc.",
        u"Description": u"Google Chrome",
        u"IdentifyingNumber": u"{35790B21-ACFE-33F5-B320-9DA320D96682}",
        u"InstallDate": u"20130710"
    }),
    rdf_protodict.Dict({
        u"Version": u"7.0.1",
        u"InstallDate2": u"",
        u"Name": u"Parity Agent",
        u"Vendor": u"Bit9, Inc.",
        u"Description": u"Parity Agent",
        u"IdentifyingNumber": u"{ADC7EB41-4CC2-4FBA-8FBE-9338A9FB7666}",
        u"InstallDate": u"20130710"
    }),
    rdf_protodict.Dict({
        u"Version": u"8.0.61000",
        u"InstallDate2": u"",
        u"Name": u"Microsoft Visual C++ 2005 Redistributable (x64)",
        u"Vendor": u"Microsoft Corporation",
        u"Description": u"Microsoft Visual C++ 2005 Redistributable (x64)",
        u"IdentifyingNumber": u"{ad8a2fa1-06e7-4b0d-927d-6e54b3d3102}",
        u"InstallDate": u"20130710"
    })
]


# TODO(hanuszczak): Rename it back to `TestCmdProcessor` once new testing
# framework is properly set up.
#
# Class of this name is clashing with other `TestCmdProcessor` (declared in
# `//grr/server/grr_response_server/gui/selenium_tests/
# artifact_view_test.py`) and breaks the test class register. This should be
# fixed when the test class register is gone and new test discovery (`pytest`)
# is deployed.
class CmdProcessor(parser.CommandParser):

  output_types = [rdf_client.SoftwarePackages]
  supported_artifacts = ["TestCmdArtifact"]

  def Parse(self, cmd, args, stdout, stderr, return_val, knowledge_base):
    _ = cmd, args, stdout, stderr, return_val, knowledge_base
    packages = []
    packages.append(
        rdf_client.SoftwarePackage.Installed(
            name="Package1",
            description="Desc1",
            version="1",
            architecture="amd64"))
    packages.append(
        rdf_client.SoftwarePackage.Installed(
            name="Package2",
            description="Desc2",
            version="1",
            architecture="i386"))

    yield rdf_client.SoftwarePackages(packages=packages)

    # Also yield something random so we can test return type filtering.
    yield rdf_client_fs.StatEntry()

    # Also yield an anomaly to test that.
    yield rdf_anomaly.Anomaly(
        type="PARSER_ANOMALY", symptom="could not parse gremlins.")


class MultiProvideParser(parser.RegistryValueParser):

  output_types = [rdf_protodict.Dict]
  supported_artifacts = ["DepsProvidesMultiple"]

  def Parse(self, stat, knowledge_base):
    _ = stat, knowledge_base
    test_dict = {
        "environ_temp": rdfvalue.RDFString("tempvalue"),
        "environ_path": rdfvalue.RDFString("pathvalue")
    }
    yield rdf_protodict.Dict(test_dict)


class RaisingParser(parsers.SingleResponseParser):

  output_types = [None]
  supported_artifacts = ["RaisingArtifact"]

  def ParseResponse(self, knowledge_base, response, path_type):
    del knowledge_base, response, path_type  # Unused.
    raise parsers.ParseError("It was bound to happen.")


# TODO: These should be defined next to the test they are used in
# once the metaclass registry madness is resolved.

# pylint: disable=function-redefined


class FooAction(server_stubs.ClientActionStub):

  in_rdfvalue = None
  out_rdfvalues = [rdfvalue.RDFString]


action_registry.RegisterAdditionalTestClientAction(FooAction)


class FooAction(actions.ActionPlugin):

  in_rdfvalue = None
  out_rdfvalues = [rdfvalue.RDFString]

  def Run(self, args):
    del args  # Unused.
    self.SendReply(rdfvalue.RDFString("zażółć gęślą jaźń 🎮"))


# pylint: enable=function-redefined


class ArtifactTest(flow_test_lib.FlowTestsBaseclass):
  """Helper class for tests using artifacts."""

  def setUp(self):
    """Make sure things are initialized."""
    super(ArtifactTest, self).setUp()
    # Common group of mocks used by lots of tests.
    self.client_mock = action_mocks.ActionMock(
        searching.Find,
        searching.Grep,
        standard.HashBuffer,
        standard.HashFile,
        standard.ListDirectory,
        standard.GetFileStat,
        standard.TransferBuffer,
    )

    patcher = artifact_test_lib.PatchDefaultArtifactRegistry()
    patcher.start()
    self.addCleanup(patcher.stop)

  def LoadTestArtifacts(self):
    """Add the test artifacts in on top of whatever is in the registry."""
    artifact_registry.REGISTRY.AddFileSource(
        os.path.join(config.CONFIG["Test.data_dir"], "artifacts",
                     "test_artifacts.json"))

  class MockClient(action_mocks.MemoryClientMock):

    def WmiQuery(self, _):
      return WMI_SAMPLE

  def RunCollectorAndGetResults(self,
                                artifact_list,
                                client_mock=None,
                                client_id=None,
                                **kw):
    """Helper to handle running the collector flow."""
    if client_mock is None:
      client_mock = self.MockClient(client_id=client_id)

    session_id = flow_test_lib.TestFlowHelper(
        collectors.ArtifactCollectorFlow.__name__,
        client_mock=client_mock,
        client_id=client_id,
        artifact_list=artifact_list,
        token=self.token,
        **kw)

    return flow_test_lib.GetFlowResults(client_id, session_id)


class GRRArtifactTest(ArtifactTest):

  def testUploadArtifactYamlFileAndDumpToYaml(self):
    artifact_registry.REGISTRY.ClearRegistry()
    artifact_registry.REGISTRY.ClearSources()
    artifact_registry.REGISTRY._CheckDirty()

    try:

      test_artifacts_file = os.path.join(config.CONFIG["Test.data_dir"],
                                         "artifacts", "test_artifacts.json")

      with io.open(test_artifacts_file, mode="r", encoding="utf-8") as filedesc:
        artifact.UploadArtifactYamlFile(filedesc.read())
      loaded_artifacts = artifact_registry.REGISTRY.GetArtifacts()
      self.assertGreaterEqual(len(loaded_artifacts), 20)
      self.assertIn("DepsWindirRegex", [a.name for a in loaded_artifacts])

      # Now dump back to YAML.
      yaml_data = artifact_registry.REGISTRY.DumpArtifactsToYaml()
      for snippet in [
          "name: TestFilesArtifact",
          "urls:\\s*- https://msdn.microsoft.com/en-us/library/",
          "returned_types:\\s*- SoftwarePackage",
          "args:\\s*- --list",
          "cmd: /usr/bin/dpkg",
      ]:
        self.assertRegex(yaml_data, snippet)
    finally:
      artifact.LoadArtifactsOnce()

  def testUploadArtifactYamlFileMissingDoc(self):
    content = """name: Nodoc
sources:
- type: GREP
  attributes:
    paths: [/etc/blah]
    content_regex_list: ["stuff"]
supported_os: [Linux]
"""
    with self.assertRaises(rdf_artifacts.ArtifactDefinitionError):
      artifact.UploadArtifactYamlFile(content)

  def testUploadArtifactYamlFileBadList(self):
    content = """name: BadList
doc: here's the doc
sources:
- type: GREP
  attributes:
    paths: /etc/blah
    content_regex_list: ["stuff"]
supported_os: [Linux]
"""
    with self.assertRaises(rdf_artifacts.ArtifactDefinitionError):
      artifact.UploadArtifactYamlFile(content)

  def testUploadArtifactYamlFileMissingNamesAttribute(self):
    content = """name: BadGroupMissingNames
doc: broken
sources:
- type: ARTIFACT_GROUP
  attributes:
    - 'One'
    - 'Two'
supported_os: [Linux]
"""

    with self.assertRaises(rdf_artifacts.ArtifactDefinitionError):
      artifact.UploadArtifactYamlFile(content)

  def testCommandArgumentOrderIsPreserved(self):
    content = """name: CommandOrder
doc: here's the doc
sources:
- type: COMMAND
  attributes:
    args: ["-L", "-v", "-n"]
    cmd: /sbin/iptables
supported_os: [Linux]
"""
    artifact.UploadArtifactYamlFile(content)
    artifact_obj = artifact_registry.REGISTRY.GetArtifacts(
        name_list=["CommandOrder"]).pop()
    arglist = artifact_obj.sources[0].attributes.get("args")
    self.assertEqual(arglist, ["-L", "-v", "-n"])

    # Check serialize/deserialize doesn't change order.
    serialized = artifact_obj.SerializeToBytes()
    artifact_obj = rdf_artifacts.Artifact.FromSerializedBytes(serialized)
    arglist = artifact_obj.sources[0].attributes.get("args")
    self.assertEqual(arglist, ["-L", "-v", "-n"])

  def testSystemArtifactOverwrite(self):
    content = """
name: WMIActiveScriptEventConsumer
doc: here's the doc
sources:
- type: COMMAND
  attributes:
    args: ["-L", "-v", "-n"]
    cmd: /sbin/iptables
supported_os: [Linux]
"""
    artifact_registry.REGISTRY.ClearRegistry()
    artifact_registry.REGISTRY.ClearSources()
    artifact_registry.REGISTRY._CheckDirty()

    # System artifacts come from the test file.
    self.LoadTestArtifacts()

    # WMIActiveScriptEventConsumer is a system artifact, we can't overwrite it.
    with self.assertRaises(rdf_artifacts.ArtifactDefinitionError):
      artifact.UploadArtifactYamlFile(content)

    # Override the check and upload anyways. This simulates the case
    # where an artifact ends up shadowing a system artifact somehow -
    # for example when the system artifact was created after the
    # artifact was uploaded to the data store for testing.
    artifact.UploadArtifactYamlFile(content, overwrite_system_artifacts=True)

    # The shadowing artifact is at this point stored in the data store. On the
    # next full reload of the registry, there will be an error that we can't
    # overwrite the system artifact. The artifact should automatically get
    # deleted from the data store to mitigate the problem.
    with self.assertRaises(rdf_artifacts.ArtifactDefinitionError):
      artifact_registry.REGISTRY._ReloadArtifacts()

    # As stated above, now this should work.
    artifact_registry.REGISTRY._ReloadArtifacts()

    # Make sure the artifact is now loaded and it's the version from the file.
    self.assertIn("WMIActiveScriptEventConsumer",
                  artifact_registry.REGISTRY._artifacts)
    artifact_obj = artifact_registry.REGISTRY.GetArtifact(
        "WMIActiveScriptEventConsumer")
    self.assertStartsWith(artifact_obj.loaded_from, "file:")

    # The artifact is gone from the data store.
    with self.assertRaises(db.UnknownArtifactError):
      data_store.REL_DB.ReadArtifact("WMIActiveScriptEventConsumer")

  def testUploadArtifactBadDependencies(self):
    yaml_artifact = """
name: InvalidArtifact
doc: An artifact group with invalid dependencies.
sources:
- type: ARTIFACT_GROUP
  attributes:
    names:
      - NonExistingArtifact
"""
    with self.assertRaises(rdf_artifacts.ArtifactDependencyError):
      artifact.UploadArtifactYamlFile(yaml_artifact)


class ArtifactFlowLinuxTest(ArtifactTest):

  def setUp(self):
    """Make sure things are initialized."""
    super(ArtifactFlowLinuxTest, self).setUp()
    users = [
        rdf_client.User(username="gogol"),
        rdf_client.User(username="gevulot"),
        rdf_client.User(username="exomemory"),
        rdf_client.User(username="user1"),
        rdf_client.User(username="user2"),
    ]
    self.SetupClient(0, system="Linux", os_version="12.04", users=users)

    self.LoadTestArtifacts()

  @parser_test_lib.WithParser("Cmd", CmdProcessor)
  def testCmdArtifact(self):
    """Check we can run command based artifacts and get anomalies."""
    client_id = test_lib.TEST_CLIENT_ID
    client_mock = self.MockClient(standard.ExecuteCommand, client_id=client_id)
    with utils.Stubber(subprocess, "Popen", client_test_lib.Popen):
      session_id = flow_test_lib.TestFlowHelper(
          collectors.ArtifactCollectorFlow.__name__,
          client_mock,
          client_id=client_id,
          use_tsk=False,
          artifact_list=["TestCmdArtifact"],
          token=self.token)

    results = flow_test_lib.GetFlowResults(client_id, session_id)
    self.assertLen(results, 2)
    packages = [
        p for p in results if isinstance(p, rdf_client.SoftwarePackages)
    ]
    self.assertLen(packages, 1)

    anomalies = [a for a in results if isinstance(a, rdf_anomaly.Anomaly)]
    self.assertLen(anomalies, 1)
    self.assertIn("gremlin", anomalies[0].symptom)

  def testFilesArtifact(self):
    """Check GetFiles artifacts."""
    client_id = test_lib.TEST_CLIENT_ID
    with vfs_test_lib.FakeTestDataVFSOverrider():
      self.RunCollectorAndGetResults(["TestFilesArtifact"],
                                     client_mock=self.client_mock,
                                     client_id=client_id)
      cp = db.ClientPath.OS(client_id, ("var", "log", "auth.log"))
      fd = file_store.OpenFile(cp)
      self.assertNotEmpty(fd.read())

  @parser_test_lib.WithParser("Passwd", linux_file_parser.PasswdBufferParser)
  def testLinuxPasswdHomedirsArtifact(self):
    """Check LinuxPasswdHomedirs artifacts."""
    with vfs_test_lib.FakeTestDataVFSOverrider():
      fd = self.RunCollectorAndGetResults(["LinuxPasswdHomedirs"],
                                          client_mock=self.client_mock,
                                          client_id=test_lib.TEST_CLIENT_ID)

      self.assertLen(fd, 5)
      self.assertCountEqual(
          [x.username for x in fd],
          [u"exomemory", u"gevulot", u"gogol", u"user1", u"user2"])
      for user in fd:
        if user.username == u"exomemory":
          self.assertEqual(user.full_name, u"Never Forget (admin)")
          self.assertEqual(user.gid, 47)
          self.assertEqual(user.homedir, u"/var/lib/exomemory")
          self.assertEqual(user.shell, u"/bin/sh")
          self.assertEqual(user.uid, 46)

  def testArtifactOutput(self):
    """Check we can run command based artifacts."""
    client_id = test_lib.TEST_CLIENT_ID
    with vfs_test_lib.VFSOverrider(rdf_paths.PathSpec.PathType.OS,
                                   vfs_test_lib.FakeTestDataVFSHandler):
      # Will raise if something goes wrong.
      self.RunCollectorAndGetResults(["TestFilesArtifact"],
                                     client_mock=self.client_mock,
                                     client_id=client_id)

      # Will raise if something goes wrong.
      self.RunCollectorAndGetResults(["TestFilesArtifact"],
                                     client_mock=self.client_mock,
                                     client_id=client_id,
                                     split_output_by_artifact=True)

      # Test the error_on_no_results option.
      with self.assertRaises(RuntimeError) as context:
        with test_lib.SuppressLogs():
          self.RunCollectorAndGetResults(["NullArtifact"],
                                         client_mock=self.client_mock,
                                         client_id=client_id,
                                         split_output_by_artifact=True,
                                         error_on_no_results=True)
      if "collector returned 0 responses" not in str(context.exception):
        raise RuntimeError("0 responses should have been returned")

  @parser_test_lib.WithParser("Raising", RaisingParser)
  def testFailuresAreLogged(self):
    client_id = "C.4815162342abcdef"

    now = rdfvalue.RDFDatetime.Now()
    data_store.REL_DB.WriteClientMetadata(client_id=client_id, last_ping=now)

    snapshot = rdf_objects.ClientSnapshot(client_id=client_id)
    snapshot.knowledge_base.os = "fakeos"
    data_store.REL_DB.WriteClientSnapshot(snapshot)

    raising_artifact_source = rdf_artifacts.ArtifactSource(
        type=rdf_artifacts.ArtifactSource.SourceType.COMMAND,
        attributes={
            "cmd": "/bin/echo",
            "args": ["1"],
        })

    raising_artifact = rdf_artifacts.Artifact(
        name="RaisingArtifact",
        doc="Lorem ipsum.",
        sources=[raising_artifact_source])

    registry = artifact_registry.ArtifactRegistry()
    with mock.patch.object(artifact_registry, "REGISTRY", registry):
      registry.RegisterArtifact(raising_artifact)

      flow_id = flow_test_lib.TestFlowHelper(
          collectors.ArtifactCollectorFlow.__name__,
          client_mock=action_mocks.ActionMock(standard.ExecuteCommand),
          client_id=client_id,
          artifact_list=["RaisingArtifact"],
          apply_parsers=True,
          check_flow_errors=True,
          token=self.token)

    results = flow_test_lib.GetFlowResults(client_id=client_id, flow_id=flow_id)
    self.assertEmpty(results)

    logs = data_store.REL_DB.ReadFlowLogEntries(
        client_id=client_id, flow_id=flow_id, offset=0, count=1024)

    # Log should contain two entries. First one about successful execution of
    # the command (not interesting), the other one containing the error about
    # unsuccessful parsing.
    self.assertLen(logs, 2)
    self.assertIn("It was bound to happen.", logs[1].message)


class ArtifactFlowWindowsTest(ArtifactTest):

  def setUp(self):
    """Make sure things are initialized."""
    super(ArtifactFlowWindowsTest, self).setUp()
    self.SetupClient(0, system="Windows", os_version="6.2", arch="AMD64")
    self.LoadTestArtifacts()

  @parser_test_lib.WithParser("WmiInstalledSoftware",
                              wmi_parser.WMIInstalledSoftwareParser)
  def testWMIQueryArtifact(self):
    """Check we can run WMI based artifacts."""
    client_id = self.SetupClient(
        0, system="Windows", os_version="6.2", arch="AMD64")
    col = self.RunCollectorAndGetResults(["WMIInstalledSoftware"],
                                         client_id=client_id)

    self.assertLen(col, 1)
    package_list = col[0]
    self.assertLen(package_list.packages, 3)
    descriptions = [package.description for package in package_list.packages]
    self.assertIn("Google Chrome", descriptions)


class GrrKbTest(ArtifactTest):

  def _RunKBI(self, **kw):
    session_id = flow_test_lib.TestFlowHelper(
        artifact.KnowledgeBaseInitializationFlow.__name__,
        self.client_mock,
        client_id=test_lib.TEST_CLIENT_ID,
        token=self.token,
        **kw)

    results = flow_test_lib.GetFlowResults(test_lib.TEST_CLIENT_ID, session_id)
    self.assertLen(results, 1)
    return results[0]


class GrrKbWindowsTest(GrrKbTest):

  def setUp(self):
    super(GrrKbWindowsTest, self).setUp()
    self.SetupClient(0, system="Windows", os_version="6.2", arch="AMD64")

    os_overrider = vfs_test_lib.VFSOverrider(rdf_paths.PathSpec.PathType.OS,
                                             vfs_test_lib.FakeFullVFSHandler)
    os_overrider.Start()
    self.addCleanup(os_overrider.Stop)

    reg_overrider = vfs_test_lib.VFSOverrider(
        rdf_paths.PathSpec.PathType.REGISTRY,
        vfs_test_lib.FakeRegistryVFSHandler)
    reg_overrider.Start()
    self.addCleanup(reg_overrider.Stop)

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseRetrievalWindows(self):
    """Check we can retrieve a knowledge base from a client."""
    kb = self._RunKBI()

    self.assertEqual(kb.environ_systemroot, "C:\\Windows")
    self.assertEqual(kb.time_zone, "US/Alaska")
    self.assertEqual(kb.code_page, "cp_1252")

    self.assertEqual(kb.environ_windir, "C:\\Windows")
    self.assertEqual(kb.environ_profilesdirectory, "C:\\Users")
    self.assertEqual(kb.environ_allusersprofile, "C:\\Users\\All Users")
    self.assertEqual(kb.environ_allusersappdata, "C:\\ProgramData")
    self.assertEqual(kb.environ_temp, "C:\\Windows\\TEMP")
    self.assertEqual(kb.environ_systemdrive, "C:")

    self.assertCountEqual([x.username for x in kb.users], ["jim", "kovacs"])
    user = kb.GetUser(username="jim")
    self.assertEqual(user.username, "jim")
    self.assertEqual(user.sid, "S-1-5-21-702227068-2140022151-3110739409-1000")

  @parser_test_lib.WithParser("MultiProvide", MultiProvideParser)
  def testKnowledgeBaseMultiProvides(self):
    """Check we can handle multi-provides."""
    # Replace some artifacts with test one that will run the MultiProvideParser.
    self.LoadTestArtifacts()
    with test_lib.ConfigOverrider(
        {"Artifacts.knowledge_base": ["DepsProvidesMultiple"]}):
      kb = self._RunKBI()

      self.assertEqual(kb.environ_temp, "tempvalue")
      self.assertEqual(kb.environ_path, "pathvalue")

  def testGlobRegistry(self):
    """Test that glob works on registry."""
    client_id = test_lib.TEST_CLIENT_ID
    paths = [
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT"
        "\\CurrentVersion\\ProfileList\\ProfilesDirectory",
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT"
        "\\CurrentVersion\\ProfileList\\AllUsersProfile"
    ]

    flow_test_lib.TestFlowHelper(
        filesystem.Glob.__name__,
        self.client_mock,
        paths=paths,
        pathtype=rdf_paths.PathSpec.PathType.REGISTRY,
        client_id=client_id,
        token=self.token)
    path = paths[0].replace("\\", "/")

    path_info = data_store.REL_DB.ReadPathInfo(
        client_id,
        rdf_objects.PathInfo.PathType.REGISTRY,
        components=tuple(path.split("/")))
    self.assertEqual(path_info.stat_entry.registry_data.GetValue(),
                     "%SystemDrive%\\Users")

  @parser_test_lib.WithAllParsers
  def testGetKBDependencies(self):
    """Test that KB dependencies are calculated correctly."""
    artifact_registry.REGISTRY.ClearSources()
    try:
      test_artifacts_file = os.path.join(config.CONFIG["Test.data_dir"],
                                         "artifacts", "test_artifacts.json")
      artifact_registry.REGISTRY.AddFileSource(test_artifacts_file)

      with test_lib.ConfigOverrider({
          "Artifacts.knowledge_base": [
              "DepsParent", "DepsDesktop", "DepsHomedir", "DepsWindir",
              "DepsWindirRegex", "DepsControlSet", "FakeArtifact"
          ],
          "Artifacts.knowledge_base_additions": ["DepsHomedir2"],
          "Artifacts.knowledge_base_skip": ["DepsWindir"],
          "Artifacts.knowledge_base_heavyweight": ["FakeArtifact"]
      }):
        args = artifact.KnowledgeBaseInitializationArgs(lightweight=True)
        kb_init = artifact.KnowledgeBaseInitializationFlow(
            rdf_flow_objects.Flow(args=args))
        kb_init.state["all_deps"] = set()
        kb_init.state["awaiting_deps_artifacts"] = []
        kb_init.state["knowledge_base"] = rdf_client.KnowledgeBase(os="Windows")
        no_deps = kb_init.GetFirstFlowsForCollection()

        self.assertCountEqual(no_deps, ["DepsControlSet", "DepsHomedir2"])
        self.assertCountEqual(kb_init.state.all_deps, [
            "users.homedir", "users.desktop", "users.username",
            "environ_windir", "current_control_set"
        ])
        self.assertCountEqual(
            kb_init.state.awaiting_deps_artifacts,
            ["DepsParent", "DepsDesktop", "DepsHomedir", "DepsWindirRegex"])
    finally:
      artifact.LoadArtifactsOnce()

  def _RunKBIFlow(self, artifact_list):
    self.LoadTestArtifacts()
    with test_lib.ConfigOverrider({"Artifacts.knowledge_base": artifact_list}):
      logging.disable(logging.CRITICAL)
      try:
        session_id = flow_test_lib.TestFlowHelper(
            artifact.KnowledgeBaseInitializationFlow.__name__,
            self.client_mock,
            client_id=test_lib.TEST_CLIENT_ID,
            token=self.token)
      finally:
        logging.disable(logging.NOTSET)
    return session_id

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseNoProvides(self):
    with self.assertRaises(RuntimeError) as context:
      self._RunKBIFlow(["NoProvides"])

    self.assertIn("does not have a provide", str(context.exception))

  def testKnowledgeBaseMultipleProvidesNoDict(self):
    with self.assertRaises(RuntimeError) as context:
      self._RunKBIFlow(["TooManyProvides"])

    self.assertIn("multiple provides clauses", str(context.exception))


class GrrKbLinuxTest(GrrKbTest):

  def setUp(self):
    super(GrrKbLinuxTest, self).setUp()
    self.SetupClient(0, system="Linux", os_version="12.04")

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseRetrievalLinux(self):
    """Check we can retrieve a Linux kb."""
    with test_lib.ConfigOverrider({
        "Artifacts.knowledge_base": [
            "LinuxWtmp", "NetgroupConfiguration", "LinuxPasswdHomedirs",
            "LinuxReleaseInfo"
        ],
        "Artifacts.netgroup_filter_regexes": ["^login$"],
        "Artifacts.netgroup_user_blacklist": ["isaac"]
    }):
      with vfs_test_lib.FakeTestDataVFSOverrider():
        with test_lib.SuppressLogs():
          kb = self._RunKBI()

    self.assertEqual(kb.os_major_version, 14)
    self.assertEqual(kb.os_minor_version, 4)
    # user 1,2,3 from wtmp. yagharek from netgroup.
    self.assertCountEqual([x.username for x in kb.users],
                          ["user1", "user2", "user3", "yagharek"])
    user = kb.GetUser(username="user1")
    self.assertEqual(user.last_logon.AsSecondsSinceEpoch(), 1296552099)
    self.assertEqual(user.homedir, "/home/user1")

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseRetrievalLinuxPasswd(self):
    """Check we can retrieve a Linux kb."""
    with vfs_test_lib.FakeTestDataVFSOverrider():
      with test_lib.ConfigOverrider({
          "Artifacts.knowledge_base": [
              "LinuxWtmp", "LinuxPasswdHomedirs", "LinuxReleaseInfo"
          ],
          "Artifacts.knowledge_base_additions": [],
          "Artifacts.knowledge_base_skip": []
      }):
        with test_lib.SuppressLogs():
          kb = self._RunKBI()

    self.assertEqual(kb.os_major_version, 14)
    self.assertEqual(kb.os_minor_version, 4)
    # user 1,2,3 from wtmp.
    self.assertCountEqual([x.username for x in kb.users],
                          ["user1", "user2", "user3"])
    user = kb.GetUser(username="user1")
    self.assertEqual(user.last_logon.AsSecondsSinceEpoch(), 1296552099)
    self.assertEqual(user.homedir, "/home/user1")

    user = kb.GetUser(username="user2")
    self.assertEqual(user.last_logon.AsSecondsSinceEpoch(), 1296552102)
    self.assertEqual(user.homedir, "/home/user2")

    self.assertFalse(kb.GetUser(username="buguser3"))

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseRetrievalLinuxNoUsers(self):
    """Cause a users.username dependency failure."""
    with test_lib.ConfigOverrider({
        "Artifacts.knowledge_base": [
            "NetgroupConfiguration", "NssCacheLinuxPasswdHomedirs",
            "LinuxReleaseInfo"
        ],
        "Artifacts.netgroup_filter_regexes": ["^doesntexist$"]
    }):
      with vfs_test_lib.FakeTestDataVFSOverrider():
        with test_lib.SuppressLogs():
          kb = self._RunKBI(require_complete=False)

    self.assertEqual(kb.os_major_version, 14)
    self.assertEqual(kb.os_minor_version, 4)
    self.assertCountEqual([x.username for x in kb.users], [])

  def testUnicodeValues(self):

    foo_artifact_source = rdf_artifacts.ArtifactSource(
        type=rdf_artifacts.ArtifactSource.SourceType.GRR_CLIENT_ACTION,
        attributes={"client_action": "FooAction"})

    foo_artifact = rdf_artifacts.Artifact(
        name="Foo",
        doc="Foo bar baz.",
        sources=[foo_artifact_source],
        provides=["os"],
        labels=["System"],
        supported_os=["Linux"])

    with artifact_test_lib.PatchCleanArtifactRegistry():
      artifact_registry.REGISTRY.RegisterArtifact(foo_artifact)

      with test_lib.ConfigOverrider({"Artifacts.knowledge_base": ["Foo"]}):
        session_id = flow_test_lib.TestFlowHelper(
            artifact.KnowledgeBaseInitializationFlow.__name__,
            client_mock=action_mocks.ActionMock(FooAction),
            client_id=test_lib.TEST_CLIENT_ID,
            token=self.token)

    results = flow_test_lib.GetFlowResults(test_lib.TEST_CLIENT_ID, session_id)
    self.assertLen(results, 1)
    self.assertEqual(results[0].os, "zażółć gęślą jaźń 🎮")


class GrrKbDarwinTest(GrrKbTest):

  def setUp(self):
    super(GrrKbDarwinTest, self).setUp()
    self.SetupClient(0, system="Darwin", os_version="10.9")

  @parser_test_lib.WithAllParsers
  def testKnowledgeBaseRetrievalDarwin(self):
    """Check we can retrieve a Darwin kb."""
    with test_lib.ConfigOverrider({"Artifacts.knowledge_base": ["MacOSUsers"]}):
      with vfs_test_lib.VFSOverrider(rdf_paths.PathSpec.PathType.OS,
                                     vfs_test_lib.ClientVFSHandlerFixture):
        kb = self._RunKBI()

    self.assertEqual(kb.os_major_version, 10)
    self.assertEqual(kb.os_minor_version, 9)
    # scalzi from /Users dir listing.
    self.assertCountEqual([x.username for x in kb.users], ["scalzi"])
    user = kb.GetUser(username="scalzi")
    self.assertEqual(user.homedir, "/Users/scalzi")


def main(argv):
  # Run the full test suite
  test_lib.main(argv)


if __name__ == "__main__":
  app.run(main)
