# 688. Knight Probability in Chessboard
# https://leetcode.com/problems/knight-probability-in-chessboard/

# Date: Mar 30, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def dp(self, x, y, n, k, visited):
        # if the knight moved off the chessboard
        if (x < 0 or x >= n) or (y < 0 or y >= n):
            return 0
        # if the night is still inside the board and made all the moves
        elif k == 0:
            return 1
        # if the state is already computed, return the cached result
        if (x, y, k) in visited:
            return visited[(x, y, k)]

        # define all the possible moves
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # initialize the probability and iterate through all possible moves
        prob = 0
        for dx, dy in moves:
            prob += self.dp(x + dx, y + dy, n, k - 1, visited) * 0.125

        # cache the computed probability
        visited[(x, y, k)] = prob

        return prob

    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        return self.dp(row, column, n, k, {})

# Test case
solution = Solution()

n = 3; k = 2; row = 0; column = 0
result = solution.knightProbability(n, k, row, column)

print(result) # 0.0625
