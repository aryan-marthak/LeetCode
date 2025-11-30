# 1219. Path with Maximum Gold

# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

#     Every time you are located in a cell you will collect all the gold in that cell.
#     From your position, you can walk one step to the left, right, up, or down.
#     You can't visit the same cell more than once.
#     Never visit a cell with 0 gold.
#     You can start and stop collecting gold from any position in the grid that has some gold.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if (r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0):
                return 0
            temp = grid[r][c]
            grid[r][c] = 0
            res = 0
            res = max(res, temp + dfs(r + 1, c))
            res = max(res, temp + dfs(r - 1, c))
            res = max(res, temp + dfs(r, c + 1))
            res = max(res, temp + dfs(r, c - 1))
            grid[r][c] = temp
            return res
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res