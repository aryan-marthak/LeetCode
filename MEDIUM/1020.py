# 1020. Number of Enclaves

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if (i < 0 or j < 0 or i == m or j == n or not grid[i][j] or (i, j) in visit):
                return 0
            visit.add((i, j))
            res = 1
            res += dfs(i + 1, j)
            res += dfs(i - 1, j)
            res += dfs(i, j + 1)
            res += dfs(i, j - 1)
            return res

        visit = set() 
        total, border = 0, 0
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                if (grid[i][j] and (i, j) not in visit and (i == 0 or i == m-1 or j == 0 or j == n-1)):
                    border += dfs(i, j)
        
        return total - border