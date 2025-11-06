# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0]) 
        island = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            # if i >= 1:
            #     dfs(i - 1, j)
            # if j >= 1:
            #     dfs(i, j - 1)
            # if i + 1 < m:
            #     dfs(i + 1, j)
            # if j + 1 < n:
            #     dfs(i, j + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)

        return island