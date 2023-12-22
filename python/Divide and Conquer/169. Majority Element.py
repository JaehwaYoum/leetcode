# 169. Majority Element
# https://leetcode.com/problems/majority-element/

# Date: Dec 18, 2023
# Difficulty: Easy

# Solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        return [b, a][nums.count(a) > half]

# Test case
solution = Solution()
nums = [2,2,1,1,1,2,2]
result = solution.majorityElement(nums)
print(result) # 2