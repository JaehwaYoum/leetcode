# 55. Jump Game
# https://leetcode.com/problems/jump-game/

# Date: Aug 31, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = nums[0]

        for i in range(1,len(nums)):
            if check ==0:
                return False
            check -= 1
            check = max(check, nums[i])
        return True

# Test case
solution = Solution()

nums =[3,2,1,0,0]
result = solution.canJump(nums)
print(result)