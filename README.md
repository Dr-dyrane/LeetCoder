# LeetCode Solutions

## Overview
This repository contains solutions to various LeetCode coding challenges implemented in Python. The solutions are organized into a Python class named `Solution`, which encapsulates functions for different problem types.

## Tasks Accomplished
- [x] **Two Sums:** Find indices of two numbers in the array that add up to a target value.
- [x] **Three Sums:** Find all unique triplets in a sorted array that add up to zero.

## Table of Contents
1. [Two Sums](#two-sums)
2. [Three Sums](#three-sums)

## Two Sums
### Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

#### Function Signature
```python
def twosums(self, x, y):
    """
    Find and return the indices of two numbers in the given array
    'x' that add up to the target value 'y'.

    Parameters:
    - x (list): The input array of integers.
    - y (int): The target sum value.

    Returns:
    - list or None: A list containing the indices of the two numbers
        that add up to 'y', or None if no such pair is found.
    """
```

#### Example Usage
```python
# Instantiate the Solution class
solver = Solution()

# Example 1
result = solver.twosums([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

# Example 2
result = solver.twosums([3, 2, 4], 6)
print(result)  # Output: [1, 2]
```

## Three Sums
### Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

#### Function Signature
```python
def threesums(self, x):
    """
    Find all unique triplets in the sorted array 'x' that add up to zero.

    Parameters:
    - x (list): A sorted array of integers.

    Returns:
    - list: A list containing lists of triplets that add up to zero.
    """
```

#### Example Usage
```python
# Instantiate the Solution class
solver = Solution()

# Example
result = solver.threesums([-1, 0, 1, 2, -1, -4])
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Contributing
Contributions to this repository are welcome. If you have additional solutions or improvements, feel free to create a pull request.

## License
This repository is licensed under the [MIT License](LICENSE).
