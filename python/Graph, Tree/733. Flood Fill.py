# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/description/

# Date: Nov 10, 2024
# Difficulty: Easy

# Time: O(m * n), Space: O(m * n)
# We need to visit every cell, and there is recursion
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        curr_color = image[sr][sc]

        # if curr_color is the same as color, return image
        if curr_color == color:
            return image

        # define dfs to change adjacent pixels
        def dfs(r, c):
            # boundary conditions 
            # if we go outside the grid, or the pixel is not curr_color, return
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != curr_color:
                return

            # if the pixel is curr_color, change it to color 
            if image[r][c] == curr_color:
                image[r][c] = color

            # call for adjacent pixels 
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)


        # start from (sr, sc) and return the changed image
        dfs(sr, sc)
        return image


# Test case
solution = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1; sc = 1; color = 2
result = solution.floodFill(image, sr, sc, color)
print(result) # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]