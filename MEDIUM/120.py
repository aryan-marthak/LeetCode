# 120. Triangle

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for i in triangle[::-1]:
            for x, y in enumerate(i):
                dp[x] = y + min(dp[x], dp[x + 1])
        return dp[0]

        # dp = triangle[-1][:]

        # for i in range(len(triangle) - 2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        # return dp[0]