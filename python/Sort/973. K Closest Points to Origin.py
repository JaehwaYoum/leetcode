# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

# Date: Dec 27, 2023
# Difficulty: Medium

# Solution 1: heap
import heapq
class Solution1(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for (x, y) in points:
            d = x**2 + y**2
            heapq.heappush(heap, (d, x, y))

        result = []
        for _ in range(k):
            (d, x, y) = heapq.heappop(heap)
            result.append([x, y])

        return result

# Solution 2: heappushpop
class Solution2(object):
    def kClosest(self, points, k):
        heap = []
        for (x, y) in points:
            d = - (x**2 + y**2) # change to max heap to use heappushpop

            if len(heap) == k:
                heapq.heappushpop(heap, (d, x, y)) # smallest value pops out and new value is added
            else:
                heapq.heappush(heap, (d, x, y))

        return [[x, y] for (d, x, y) in heap]

# Solution 3: one line
class Solution3(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)

# Test case
solution = Solution3()
points = [[3,3],[5,-1],[-2,4]]
k = 2
result = solution.kClosest(points, k)
print(result) # [[3, 3], [-2, 4]]