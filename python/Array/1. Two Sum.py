# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Date: Oct 5, 2023
# Difficulty: Easy

# Solution 1
# Time: O(n^2), Space: O(1)
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twosum = nums[i] + nums[j]
                if twosum == target:
                    start = i
                    end = j
                    break

        return [start, end]

# Solution 2
# Time: O(n), Space: O(n)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_map = {}
        for i, v in enumerate(nums):
            if target-v in nums_map:
                return [nums_map[target-v], i]
            nums_map[v] = i

# Test case
solution = Solution2()

nums = [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(result)
