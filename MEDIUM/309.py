# 309. Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

#     After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, txn):
            if i >= len(prices):
                return 0
            if (i, txn) in dp:
                return dp[(i, txn)]
            cooldown = dfs(i + 1, txn)
            if txn:
                buy = dfs(i + 1, not txn) - prices[i]
                dp[(i, txn)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not txn) + prices[i]
                dp[(i, txn)] = max(sell, cooldown)
            return dp[(i, txn)]
        return dfs(0, True)
    
