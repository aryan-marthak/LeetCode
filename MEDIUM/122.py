# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

# Find and return the maximum profit you can achieve.

# Dynamic Programming Top Down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            res = helper(i + 1, bought)
            if bought:
                res = max(res, prices[i] + helper(i + 1, False))
            else:
                res = max(res, -prices[i] + helper(i + 1, True))
            dp[(i, bought)] = res
            return res
        return helper(0, False)

# Brute Force Recursion
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, bought):
            if i == len(prices):
                return 0
            res = helper(i + 1, bought)
            if bought:
                res = max(res, prices[i] + helper(i + 1, False))
            else:
                res = max(res, -prices[i] + helper(i + 1, True))
            return res
        return helper(0, False)
    
# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices[1:]:
            if i > buy:
                profit += i - buy
            buy = i
        return profit