# 55. Jump Game
# https://leetcode.com/problems/jump-game/

# Date: Aug 31, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n), Space: O(1)
class Solution1(object):
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

# Solution 2
# Time: O(n^2), Space: O(n)
class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                furthest_reach = i + nums[i]

                if furthest_reach >= n-1:
                    return True

                for j in range(i+1, furthest_reach):
                    dp[j] = True

        return False


# Test case
solution = Solution2()

nums =[3,2,1,0,0]
result = solution.canJump(nums)
print(result)