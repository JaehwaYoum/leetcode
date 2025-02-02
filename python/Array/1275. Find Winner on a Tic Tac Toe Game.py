# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

# Date: Jan 28, 2025
# Difficulty: Easy

# Solution
# Time: O(1), Space: O(1)
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[0] * 3 for i in range(3)]
        for i, (r, c) in enumerate(moves):
            player = "A" if i % 2 == 0 else "B"
            board[r][c] = player
        
        for player in ["A", "B"]: 
            if self.iswinner(board, player):
                return player
        
        return "Draw" if len(moves) == 9 else "Pending"

    def iswinner(self, board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        
        return False



# Test case
solution = Solution()
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
result = solution.tictactoe(moves)
print(result) # "A"
