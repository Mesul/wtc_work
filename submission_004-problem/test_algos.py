import unittest
from unittest.mock import patch
from io import StringIO
import super_algos
 

class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(super_algos.find_min([5]), 5)
        self.assertEqual(super_algos.find_min([9, 65, -4, 2]), -4)
        self.assertEqual(super_algos.find_min([]), -1)
        self.assertEqual(super_algos.find_min([5, "c", 7.6, 8, 3]), -1)
        self.assertEqual(super_algos.find_min([8, 9, 2, 4]), 2)

    def test_sum_all(self):
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([1,2,3,4,5]), 15)
        self.assertEqual(super_algos.sum_all([-5,-4,-1]), -10)
        self.assertEqual(super_algos.sum_all([3,9,6,"na",8.7]), -1)
        self.assertEqual(super_algos.find_min([3]), 3)

    def test_find_possible_strings(self):
        self.assertEqual(super_algos.find_possible_strings([3,2,7.9], 3), [])
        self.assertEqual(super_algos.find_possible_strings([], 3), [])
        self.assertEqual(super_algos.find_possible_strings(["a","b","c"], 1), ["a","b","c"])
        self.assertEqual(super_algos.find_possible_strings(['d','f',], 3), ['ddd', 'ddf','dfd','dff','fdd','fdf','ffd','fff'])


if __name__ == "__main__":
    unittest.main()