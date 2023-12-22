# 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

# Date: Dec 13, 2023
# Difficulty: Medium

import collections

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

# Test case
solution = Solution()

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
result = solution.findMinHeightTrees(n, edges)
print(result) # [1]

# Test case 2
solution2 = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
result = solution2.findMinHeightTrees(n, edges)
print(result) # [3, 4]