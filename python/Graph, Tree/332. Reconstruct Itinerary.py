# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/description/

# Date: Dec 23, 2023
# Difficulty: Hard

# Solution 1
import collections
class Solution1(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]

# Solution 2
import collections
class Solution2(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]

# Test case
solution = Solution2()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

result = solution.findItinerary(tickets)
print(result) # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
