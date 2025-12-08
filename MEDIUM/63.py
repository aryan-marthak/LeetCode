# 63. Unique Paths II

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# BRUTE FORCE - RECURSION
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c]:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            return dfs(r + 1, c) + dfs(r, c + 1)
        return dfs(0, 0)
    
# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(m - 1, n - 1) : 1}
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            if r == m - 1 and c == n - 1:
                return 1
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]
        return dfs(0, 0)