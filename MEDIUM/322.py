# 322. Coin Change

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Brute Force
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        limit = amount + 1
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return limit
            res = limit
            for c in coins:
                res = min(res, 1 + dfs(amount - c))
            return res
        return dfs(amount) if dfs(amount) != limit else -1
        
# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j])
        return dp[amount] if dp[amount] != amount + 1 else -1