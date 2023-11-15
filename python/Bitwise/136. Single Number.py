# 136. Single Number
# https://leetcode.com/problems/single-number/

# Date: Nov 15, 2023
# Difficulty: Easy

# Time: O(n), Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num

        return result

# Test case
solution = Solution()

nums = [4,1,2,1,2]
result = solution.singleNumber(nums)
print(result) # 4