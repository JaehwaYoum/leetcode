# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

# Date: Oct 11, 2024
# Difficulty: Easy

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # create sets for checking
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # iterate each number in the board to check for sudoku rules
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue

                else:
                    if num in rows[r]:
                        return False
                    else:
                        rows[r].add(num)

                    if num in cols[c]:
                        return False
                    else:
                        cols[c].add(num)

                    box_idx = (r // 3) * 3 + c // 3
                    if num in boxes[box_idx]:
                        return False
                    else:
                        boxes[box_idx].add(num)

                return True

# Test case
solution = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
target = 0
result = solution.isValidSudoku(board)
print(result) # True