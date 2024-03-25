# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/

# Date: Sep 1, 2023
# Difficulty: Medium

# Time: O(n), Space: O(1)

# Solution 1
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        j, j_max = 0, 0

        for i in range(len(nums)-1):

            if i+nums[i] > j_max:
                j_max = i+nums[i]

            if j_max >= len(nums) -1:
                count += 1
                break

            if i==j:
                count += 1
                j = j_max

        return count

# Test case
solution = Solution()

nums =[2,3,5,2,1,1,2,4,3,1]
result = solution.jump(nums)
print(result)

