# 695. Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        if not grid:
            return 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            temp = 1
            temp += dfs(r + 1, c)
            temp += dfs(r - 1, c)
            temp += dfs(r, c + 1)
            temp += dfs(r, c - 1)
            return temp

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea
    
        # BFS Approach
        # Ds = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # def bfs(r, c):
        #     q = deque()
        #     q.append((r, c))
        #     grid[r][c] = 0
        #     res = 1

        #     while q:
        #         row, col = q.popleft()
        #         for i, j in Ds:
        #             nr, nc = row + i, col + j
        #             if (nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == 0):
        #                 continue
        #             q.append((nr, nc))
        #             grid[nr][nc] = 0
        #             res += 1
        #     return res