import unittest
import sample_program

class TestSecondLargest(unittest.TestCase):
    def test_two_element_list(self):
        self.assertEqual(sample_program.second_largest_num([1, 2]), 1)


    def test_multiple_element_list(self):
        self.assertEqual(sample_program.second_largest_num([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), 6)
