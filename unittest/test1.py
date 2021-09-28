import unittest
from test import sort
class testing_sort(unittest.TestCase):

    def test_one(self):
        result = sort([6, 3, 3, 1, 7, 5, 0, -1, 1])
        self.assertEqual([-1, 0, 1, 1, 3, 3, 5, 6, 7], result)
