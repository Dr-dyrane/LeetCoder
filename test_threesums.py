import unittest
from leets import Solution

class TestThreeSumsFunction(unittest.TestCase):
    """
    A test suite for the threesums function.
    """

    def test_valid_input(self):
        """
        Test case where triplets add up to zero.
        """
        nums = [-1, 0, 1, 2, -1, -4]
        expected_result = [[-1, -1, 2], [-1, 0, 1]]
        
        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the threesums method directly from the Solution class
        result = solution.threesums(nums)
        
        self.assertEqual(sorted(result), sorted(expected_result))
        print(f"Test Case 1: Expected Result: {expected_result}, Actual Result: {result}")
        print("")

    def test_no_triplets(self):
        """
        Test case where no triplets add up to zero.
        """
        nums = [1, 2, 3]
        expected_result = []

        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the threesums method directly from the Solution class
        result = solution.threesums(nums)
        
        self.assertEqual(result, expected_result)
        print(f"Test Case 2: Expected Result: {expected_result}, Actual Result: {result}")
        print("")

if __name__ == '__main__':
    unittest.main()
