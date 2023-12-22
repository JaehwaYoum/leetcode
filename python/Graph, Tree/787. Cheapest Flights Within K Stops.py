# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Date: Nov 29, 2023
# Difficulty: Medium

# Solution 1: Dijkstra's Algorithm
# Time: O(E + n log(n)), Space: O(n)
import collections
import heapq
class Solution1(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        # u: source, v: target, w: price
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Q: priority queue (min heap)
        # 0: initial time, src: starting node, k: stops left
        Q = [(0, src, k + 1)]

        # cost: records the lowest price
        cost = collections.defaultdict(lambda: float('inf'))
        cost[(src, k + 1)] = 0

        while Q:
            price, node, stops = heapq.heappop(Q)
            if node == dst:
                return price
            if stops > 0:
                for v, w in graph[node]:
                    alt = price + w
                    # Only push to the queue if this path is cheaper than any known path to v with the same or more stops remaining
                    if alt < cost[(v, stops - 1)]:
                        cost[(v, stops - 1)] = alt
                        heapq.heappush(Q, (alt, v, stops - 1))

        return -1

# Solution 2: BFS
# Time: O(n × E), Space: O(n)
class Solution2(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        q = [(src, 0)]
        minCost = [float('inf') for _ in range(n)]
        stops = 0

        while q and stops <= k:
            size = len(q)
            for i in range(size):
                currNode, cost = q.pop(0)
                for neighbour, price in adj[currNode]:
                    if price + cost >= minCost[neighbour]:
                        continue
                    minCost[neighbour] = price + cost
                    q.append((neighbour, minCost[neighbour]))
            stops += 1

        return -1 if minCost[dst] == float('inf') else minCost[dst]


# Test case
solution = Solution1()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0; dst = 3; k = 1
result = solution.findCheapestPrice(n, flights, src, dst, k)
print(result) # 700
