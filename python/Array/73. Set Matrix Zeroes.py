# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/

# Date: Jan 5, 2025
# Difficulty: Medium

# Time: O(m * n), Space: O(m + n)
class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# Solution 2: Use first row, col to mark zeros 
# Time: O(m * n), Space: O(1)
class Solution2(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # check if first row or col needs to be zeroed 
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # mark rows to be zeroed on the first row and column 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # zero out the rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # handle the first row and col case
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Test case
solution = Solution2()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix)
print(matrix) # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]