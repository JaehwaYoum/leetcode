# 78. Subsets
# https://leetcode.com/problems/subsets/

# Date: Nov 15, 2023
# Difficulty: Medium

# Solution 1
# Time: O(2^n), Space: O(2^n)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return result

# Test case
solution = Solution()
nums = [1,2,3]
result = solution.subsets(nums)
print(result) # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

