# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# Date: Dec 23, 2023
# Difficulty: Medium

# Solution 1
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False

# Solution 2
class Solution2(object):
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

# Test case
solution = Solution2()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
result = solution.searchMatrix(matrix, target)
print(result) #True
