# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

# Date: Dec 23, 2023
# Difficulty: Medium

# Solution 1: TLE
import collections
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

# Solution 2: keeps track of the visited nodes
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

# Test case
solution = Solution2()

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
result = solution.canFinish(numCourses, prerequisites)
print(result) # True

