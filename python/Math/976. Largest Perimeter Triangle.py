# 976. Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

# Date: Jan 30, 2025
# Difficulty: Easy

# Solution
# Time: O(n log n), Space: O(1)
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True) # O(n log n) time complexity 

        # pop until we see the case where
        # one side is smaller than the sum of other two sides 
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)

        if len(nums) >= 3:
            return sum(nums[:3])
            
        return 0

        # Another version (avoiding pop())
        # for i in range(len(nums) - 2):  # O(n)
        #     if nums[i] < nums[i + 1] + nums[i + 2]:  # Triangle condition
        #         return nums[i] + nums[i + 1] + nums[i + 2]

        # return 0


# Test case
solution = Solution()

nums = [1,2,1,10]
result = solution.largestPerimeter(nums)

print(result) # 0