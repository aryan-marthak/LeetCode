# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0 
        Ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for i, j in Ds:
                dfs(r + i, c + j)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands