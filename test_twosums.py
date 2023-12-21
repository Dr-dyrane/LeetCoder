import unittest
from leets import Solution

class TestTwoSumsFunction(unittest.TestCase):
    """
    Test cases for the `twosums` function.
    """

    def test_valid_input(self):
        """
        Test case where a pair of elements adds up to the target.
        """
        x = [2, 7, 11, 15]
        y = 9
        expected_result = sorted([0, 1])

        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the twosums method directly from the Solution class
        result = solution.twosums(x, y)
        
        self.assertEqual(sorted(result), expected_result)
        print(f"Test Case 1: Expected Result: {expected_result}, Actual Result: {result}")
        print("")

    def test_invalid_input(self):
        """
        Test case where no pair of elements adds up to the target.
        """
        x = [2, 7, 11, 15]
        y = 5
        expected_result = None

        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the twosums method directly from the Solution class
        result = solution.twosums(x, y)
        
        self.assertIsNone(result)
        print(f"Test Case 2: Expected Result: {expected_result}, Actual Result: {result}")
        print("")

if __name__ == '__main__':
    unittest.main()
