import unittest


class LineSplitter:
    def split(self, param, param1):
        pass


class LineSplittingTest(unittest.TestCase):
    def test_spitting_a_line(self):
        line_splitter = LineSplitter()
        result = line_splitter.split("One,Two,Three,Four", ",")
        self.assertEqual(["One", "Two", "Three", "Four"], result)