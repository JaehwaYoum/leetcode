# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

# Date: Sep 30, 2023
# Difficulty: Easy

# Solution 1: list
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sorted(nums)[len(nums) // 2]

# Solution 2: merge sort, recursive
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b,a][nums.count(a) > half]
        # returns a if the condition is true, otherwise b

# Test case
solution = Solution2()

nums = [2,2,1,1,1,2,2]
result = solution.majorityElement(nums)
print(result)


