# 167. Two Sum II - Input Array Is Sorted 
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Date: Dec 23, 2023
# Difficulty: Medium


# Solution 1: Two pointers
class Solution1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(numbers) - 1

        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

# Solution 2: Binary Search
class Solution2(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            left, right = k, len(numbers) - k
            expected = target - v

            while left <= right:
                mid = left + (right - left)//2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, right + 1

# Solution 3: Bisect module
import bisect
class Solution3(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            # k+1 ensures the search starts from the next element in the list,
            # to avoid using the same number twice.

            # Check if the expected value was found
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1 # Return the indices that sum up to the target

# Test case
solution = Solution3()

numbers = [2,7,11,15]
target = 9
output = solution.twoSum(numbers, target)
print(output) #
