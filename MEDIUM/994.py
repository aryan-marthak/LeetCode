# 994. Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = []
        minutes = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        while rotten and fresh > 0:
            minutes += 1
            curr = []
            for x, y in rotten:
                check = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for a, b in check:
                    if a >= 0 and b >= 0 and a < m and b < n and grid[a][b] == 1:
                        grid[a][b] = 2
                        fresh -= 1
                        curr.append((a, b))
                        if fresh == 0:
                            return minutes
            rotten = curr
        if fresh == 0:
            return minutes
        else:
            return -1