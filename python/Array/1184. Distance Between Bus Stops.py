# 1184. Distance Between Bus Stops
# https://leetcode.com/problems/distance-between-bus-stops/description/

# Date: Aug 17, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start
        
        dist_start = sum(distance[:start])
        dist_dest = sum(distance[destination:])
        if sum(distance[start:destination]) < dist_start + dist_dest:
            return sum(distance[start:destination])
        else:
            return dist_start + dist_dest

# Test case
solution = Solution()

distance = [1,2,3,4]; start = 0; destination = 1
result = solution.distanceBetweenBusStops(distance, start, destination)
print(result)