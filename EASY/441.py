# 441. Arranging Coins

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            n = n - i
            if n < 0 :
                break
            count += 1
        return count