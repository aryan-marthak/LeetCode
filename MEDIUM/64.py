# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}
        def dfs(r, c):
            if r >= m or c >= n:
                return float('inf')
            if (r, c) in dp:
                return dp[(r, c)]
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            dp[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return dp[(r, c)]
        return dfs(0, 0)