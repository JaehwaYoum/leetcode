# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

# Date: Nov 29, 2023
# Difficulty: Medium

# Solution 1: Dijkstra's algorithm
# Time: O(n), Space: O(n)
import collections
import heapq
class Solution1(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # u: source, v: target, w: time
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        # Q: priority queue (min heap)
        # 0: initial time, k: starting node
        Q = [(0, k)]

        # dist: records the shortest time
        dist = collections.defaultdict(int)

        # processing nodes
        while Q:
            # pop the node with smallest accumulated time
            time, node = heapq.heappop(Q)
            # if not in dist, shortest time is recorded
            if node not in dist:
                dist[node] = time
                # if the alt path is shorter, it is added
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # checking for completion
        if len(dist) == n:
            return max(dist.values())

        return -1


# Test case
solution = Solution1()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
result = solution.networkDelayTime(times, n, k)
print(result) # 2
