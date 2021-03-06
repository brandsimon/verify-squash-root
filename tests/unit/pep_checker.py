import sys
import unittest
import pycodestyle
from pyflakes.api import checkRecursive
from pyflakes.reporter import Reporter

CHECK_FILES = ["src/", "tests/", "setup.py"]


class Pep8Test(unittest.TestCase):

    def test_pep8(self):
        style = pycodestyle.StyleGuide()
        check = style.check_files(CHECK_FILES)
        self.assertEqual(check.total_errors, 0,
                         'PEP8 errors: %d' % check.total_errors)

    def test_pyflakes(self):
        rep = Reporter(sys.stdout, sys.stderr)
        error_count = checkRecursive(CHECK_FILES, rep)
        self.assertEqual(error_count, 0,
                         'PyFlakes errors: %d' % error_count)
