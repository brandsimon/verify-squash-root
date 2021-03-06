import unittest
from unittest import mock
from verify_squash_root.mount import TmpfsMount


class MountTest(unittest.TestCase):

    def test__tmpfs_mount(self):
        base = "verify_squash_root.mount"
        all_mocks = mock.Mock()
        with (mock.patch("{}.exec_binary".format(base),
                         new=all_mocks.exec_binary),
              mock.patch("{}.os".format(base),
                         new=all_mocks.os),
              mock.patch("{}.shutil".format(base),
                         new=all_mocks.shutil)):
            call = mock.call
            with TmpfsMount("/my_directory"):
                self.assertEqual(
                    all_mocks.mock_calls,
                    [call.os.mkdir('/my_directory'),
                     call.exec_binary(['mount', '-t', 'tmpfs', '-o',
                                       'mode=0700,uid=0,gid=0', 'tmpfs',
                                       '/my_directory'])])
                all_mocks.reset_mock()
            self.assertEqual(
                all_mocks.mock_calls,
                [call.exec_binary(['umount', '-f', '-R', '/my_directory']),
                 call.shutil.rmtree('/my_directory')])
