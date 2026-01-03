# 1411. Number of Ways to Paint N × 3 Grid

# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

# OPTIMAL SOLUTION WITH MATH
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        aba = 6
        abc = 6

        for i in range(1, n):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD

            aba = next_aba
            abc = next_abc            
        return (aba + abc) % MOD
