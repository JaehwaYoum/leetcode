# 77. Combinations
# https://leetcode.com/problems/combinations/

# Date: Oct 10, 2023
# Difficulty: Medium

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)

                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result


