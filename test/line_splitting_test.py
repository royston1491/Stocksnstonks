import unittest

from line_splitter import LineSplitter


class LineSplittingTest(unittest.TestCase):
    def test_spitting_a_line(self):
        line_splitter = LineSplitter()
        result = line_splitter.split("One,Two,Three,Four", ",")
        self.assertEqual(["One", "Two", "Three", "Four"], result)