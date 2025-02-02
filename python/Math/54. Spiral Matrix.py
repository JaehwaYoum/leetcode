# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# Date: Jan 30, 2025
# Difficulty: Medium

# Solution
# Time: O(m * n), Space: O(m * n)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        i_start, j_start = 0, 0
        i_end, j_end = m-1, n-1
        result = []

        while i_start <= i_end and j_start <= j_end:
            for j in range(j_start, j_end + 1):
                result.append(matrix[i_start][j])
            i_start += 1

            for i in range(i_start, i_end + 1):
                result.append(matrix[i][j_end])
            j_end -= 1

            if i_start <= i_end:
                for j in range(j_end, j_start - 1, -1):
                    result.append(matrix[i_end][j])
                i_end -= 1
                print(result)

            if j_start <= j_end:
                for i in range(i_end, i_start - 1, -1):
                    result.append(matrix[i][j_start])
                j_start += 1
        
        return result


# Test case
solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = solution.spiralOrder(matrix)

print(result) # [1,2,3,6,9,8,7,4,5]