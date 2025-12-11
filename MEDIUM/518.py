# 518. Coin Change II

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, amount):
            if amount == 0:
                return 1
            if (i, amount) in dp:
                return dp[(i, amount)]
            if i == len(coins):
                return 0
            dp[(i, amount)] = dfs(i + 1, amount)
            if amount >= coins[i]:
                dp[(i, amount)] += dfs(i, amount - coins[i])
            return dp[(i, amount)]
        return dfs(0, amount)

