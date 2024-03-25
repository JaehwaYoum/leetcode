# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

# Date: March 25, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        n = len(mat[0])
        result = 0

        for i in range(n//2):
            result += mat[i][i] + mat[i][-i-1] + mat[-i-1][i] + mat[-i-1][-i-1]

        if n % 2 == 1:
            mid = n//2
            result += mat[mid][mid]

        return result


# Test case
solution = Solution()

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
result = solution.diagonalSum(mat)
print(result) # 25
