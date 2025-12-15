# 576. Out of Boundary Paths

# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}
        def dfs(r, c, moves):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if (r, c, moves) in dp:
                return dp[(r, c, moves)]
            if moves == 0:
                return 0
            dp[(r, c, moves)] = (dfs(r + 1, c, moves - 1) +
                          dfs(r - 1, c, moves - 1) + 
                          dfs(r, c + 1, moves - 1) + 
                          dfs(r, c - 1, moves - 1)) % mod
            return dp[(r, c, moves)]
        return dfs(startRow, startColumn, maxMove)