# 1162. As Far from Land as Possible

# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append([r, c])
        res = -1
        direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        while q:
            r, c = q.popleft()

            res = grid[r][c]
            for dr, dc in direction:
                newR, newC = r + dr, c + dc
                if (min(newR, newC) >= 0 and max(newR, newC) < N and grid[newR][newC] == 0):
                    q.append([newR, newC])
                    grid[newR][newC] = grid[r][c] + 1
        return res - 1 if res > 1 else -1