# 867. Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0

        result = [[None for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]

        return result

# Test case
solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = solution.transpose(matrix)
print(result) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
