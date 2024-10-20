# 48. Rotate Image
# https://leetcode.com/problems/rotate-image

# Date: Oct 11, 2024
# Difficulty: Easy

# Transpose -> reverse rows
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

# Ref: Rotate 90 degrees anti-clockwise
# Transpose -> reverse columns
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for col in range(n):
            for row in range(n//2):
                matrix[row][col], matrix[n-row-1][col] = matrix[n-row-1][col], matrix[row][col]

# Test case
solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = solution.rorate(matrix)
print(result) # [[7,4,1],[8,5,2],[9,6,3]]