# 695. Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_land = 0
        m = len(grid)
        n = len(grid[0])

        if not grid:
            return 0

        def dfs(m, n, max_land):
            temp = 0
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                temp += 1
                max_land = max(temp, max_land)
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, max_land)

        return max_land