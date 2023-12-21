class Solution:
    '''
    A class encapsulating solutions for LeetCode coding challenges.
    '''


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
        # Create a dictionary to store
        # the difference between the target value and each element
        d = {}

        # Enumerate through each element and its index in the array x
        for k, v in enumerate(x):
            # Calculate the difference between
            # the target value and the current element
            c = y - v

            # If the difference is already in the dictionary,
            # return the indices of the two numbers
            if c in d:
                return [d[c], k]

            # Store the current element and its index in the dictionary
            d[v] = k

        # If no such pair is found, return None
        return None


    def threesums(self, x):
        """
        Find all unique triplets in the sorted array 'x' that add up to zero.

        Parameters:
        - x (list): A sorted array of integers.

        Returns:
        - list: A list containing lists of triplets that add up to zero.
        """
        x.sort()
        result = []
        # for each element at index i in the array x, except the last two:
        for i in range(len(x) - 2):
            # if i is not the first element &
            # x[i] is the same as the previous element x[i-1]:
            if i > 0 and x[i] == x[i - 1]:
                #  skip to the next iteration
                continue

            # initialize two pointers; <-- and -->,
            # pointing to the next & last elements
            left, right = i + 1, len(x) - 1

            #  while left is to the left of right:
            while left < right:
                # calculate the sum of the elements at indices i, left, & right
                current_sum = x[i] + x[left] + x[right]

                # if the sum is 0:
                if current_sum == 0:
                    # add the triplet [x[i], x[left], x[right]] to the result
                    result.append([x[i], x[left], x[right]])

                    # skip duplicate elements on the left and right
                    while left < right and x[left] == x[left + 1]:
                        left += 1
                    while left < right and x[right] == x[right - 1]:
                        right -= 1

                    # move the left pointer to the next element
                    left += 1
                    # move the right pointer to the previous element
                    right -= 1
                #  else if the sum is less than 0:
                elif current_sum < 0:
                    # move the left pointer to the next element
                    left += 1
                # If the sum is greater than 0:
                else:
                    # move the right pointer to the previous element
                    right -= 1

        # return the result
        return result
