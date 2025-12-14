# 931. Minimum Falling Path Sum

# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(r, c):
            if r >= len(matrix):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            if c < 0 or c >= len(matrix):
                return float('inf')
            dp[(r, c)] = matrix[r][c] + min(dfs(r + 1, c - 1), dfs(r + 1, c), dfs(r + 1, c + 1))
            return dp[(r, c)]
        res = float('inf')
        for i in range(len(matrix)):
            res = min(res, dfs(0, i))
        return res