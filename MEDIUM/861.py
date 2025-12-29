# 861. Score After Flipping Matrix

# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves (including zero moves).

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 0 if grid[r][c] else 1
        for c in range(n):
            ones = 0
            for r in range(m):
                if grid[r][c] == 1:
                    ones += 1
            if ones < m - ones:
                for r in range(m):
                    grid[r][c] = 0 if grid[r][c] else 1
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    res += 2 ** (n - c - 1)
        return res