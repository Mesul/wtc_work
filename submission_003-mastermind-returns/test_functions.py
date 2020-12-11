import unittest
from unittest.mock import patch
from io import StringIO
import mastermind
import random
 

class MyTestCase(unittest.TestCase):
    def test_create_code(self):
        counter = 1
        while counter <= 100:
            self.assertEqual(len(mastermind.create_code()), 4)
            self.assertNotIn(0, mastermind.create_code())
            self.assertNotIn(9, mastermind.create_code())
            counter = counter + 1

    def test_check_correctness(self):
        self.assertEqual(mastermind.check_correctness(5, 4), True)
        self.assertEqual(mastermind.check_correctness(9, 4), True)
        self.assertEqual(mastermind.check_correctness(1, 4), True)
        self.assertEqual(mastermind.check_correctness(3, 3), False)
        self.assertEqual(mastermind.check_correctness(7, 2), False)
        self.assertEqual(mastermind.check_correctness(11, 1), False)
    
    @patch("sys.stdin", StringIO("1234\n5678\n"))
    def test_get_user_input(self):
        self.assertEqual(mastermind.get_user_input(), "1234")
        self.assertEqual(mastermind.get_user_input(), "5678")

    
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([1, 2, 3, 4], "1234"), (4, 0))
        self.assertEqual(mastermind.take_turn([5, 8, 7, 6], "6587"), (0, 4))
        self.assertEqual(mastermind.take_turn([1, 2, 3, 4], "1287"), (2, 0))
        self.assertEqual(mastermind.take_turn([1, 8, 7, 6], "1867"), (2, 2))
        self.assertEqual(mastermind.take_turn([1, 2, 3, 4], "1274"), (3, 0))
        self.assertEqual(mastermind.take_turn([2, 8, 5, 6], "8527"), (0, 3))
        self.assertEqual(mastermind.take_turn([8, 7, 4, 2], "7463"), (0, 2))
        self.assertEqual(mastermind.take_turn([3, 2, 5, 6], "3187"), (1, 0))
        self.assertEqual(mastermind.take_turn([4, 2, 5, 3], "3187"), (0, 1))


if __name__ == '__main__':
    unittest.main()