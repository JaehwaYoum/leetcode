# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

# Date: Mar 25, 2024
# Difficulty: Easy

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        sorted_nums = sorted(nums)

        for num in nums:
            idx = sorted_nums.index(num)
            result.append(idx)

        return result


# Test case
solution = Solution()

nums = [8,1,2,2,3]
result = solution.smallerNumbersThanCurrent(nums)
print(result) # [4,0,1,1,3]