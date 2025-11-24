# 1254. Number of Closed Islands

# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == m or c == n):
                return 0
            if grid[r][c] == 1 or (r, c) in visit:
                return 1
            visit.add((r, c))
            return min(dfs(r + 1, c),
            dfs(r - 1, c),
            dfs(r, c + 1),
            dfs(r, c - 1))

        count = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and (i, j) not in visit:
                   count += dfs(i, j)

        return count