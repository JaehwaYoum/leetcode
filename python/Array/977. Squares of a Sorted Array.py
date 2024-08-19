# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Date: Apr 20, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in nums])
        

# Test case
solution = Solution()
 nums = [-4,-1,0,3,10]
result = solution.sortedSquares(nums)
print(result) # [0,1,9,16,100]