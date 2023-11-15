# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# Date: Nov 15, 2023
# Difficulty: Medium

# Solution 1
# Time: O(n^target), Space: O(target)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result

# Test case
solution = Solution()
candidates = [2,3,6,7]; target = 7
result = solution.combinationSum(candidates, target)
print(result) # [[2, 2, 3], [7]]