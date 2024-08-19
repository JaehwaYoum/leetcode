# 2824. Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

# Date: Aug 19, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            if nums[left] + nums[right] < target:
                result += right - left # add all the cases
                left += 1
            else:
                right -= 1
        
        return result


# Test case
solution = Solution()
nums = [-1,1,2,3,1]; target = 2	
result = solution.countPairs(nums, target)
print(result) # 3