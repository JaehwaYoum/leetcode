# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

# Date: Sep 30, 2023
# Difficulty: Medium

# Time: O(rows * cols), Space: O(rows * cols)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return 0

            grid[row][col] = "0" # turn the checked ones to 0
            count = 1
            count += dfs(row - 1, col)
            count += dfs(row + 1, col)
            count += dfs(row, col - 1)
            count += dfs(row, col + 1)
            return count

        rows = len(grid)
        cols = len(grid[0])
        islands = 0 # count the number of islands

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_size = dfs(row, col)
                    islands += 1

        return islands

# Test case
solution = Solution()

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = solution.numIslands(grid)
print(result) #3