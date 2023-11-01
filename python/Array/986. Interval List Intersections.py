# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

# Date: Jul 12, 2023
# Difficulty: Medium

# Time: O(n^2)
# Space: O(n)

# Solution 1
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        start = 0
        end = 0
        lists = []

        for i in range(len(firstList)):
            for j in range(len(secondList)):
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])

                if start <= end:
                    temp_list = [start, end]
                    lists.append(temp_list)

        return lists

# Test case
solution = Solution()

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
result = solution.intervalIntersection(firstList,secondList)
print(result)
# [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]