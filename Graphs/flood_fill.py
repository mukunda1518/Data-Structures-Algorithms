# Leetcode: https://leetcode.com/problems/flood-fill/
# https://www.youtube.com/watch?v=C-2_uSRli8o&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=9





class Solution:

    def dfs(self, sr, sc, color, initial_color, ans, image, n, m):
        ans[sr][sc] = color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row, col in directions:
            nrow = sr + row
            ncol = sc + col
            if 0 <= nrow < n and 0 <= ncol < m and image[nrow][ncol] == initial_color and ans[nrow][ncol] != color:
                self.dfs(nrow, ncol, color, initial_color, ans, image, n, m)


    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ans = image.copy()
        initial_color = image[sr][sc]
        n = len(image)
        m = len(image[0])
        self.dfs(sr, sc, color, initial_color, ans, image, n, m)
        return ans
        