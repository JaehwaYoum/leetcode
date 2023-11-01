# 46. Permutations
# https://leetcode.com/problems/permutations/

# Date: Oct 10, 2023
# Difficulty: Medium

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []
        prev_element = []

        def dfs(element):
            if len(element) == 0:
                results.append(prev_element[:])

            for e in element:
                next_element = element[:]
                next_element.remove(e)

                prev_element.append(e)
                dfs(next_element)
                prev_element.pop()

        dfs(nums)
        return results
