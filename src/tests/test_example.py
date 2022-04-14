import unittest
from example import fun

class TestExample(unittest.TestCase):

    def test_fun(self):

        self.assertEqual(5, fun(4))
