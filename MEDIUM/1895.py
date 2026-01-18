# 1895. Largest Magic Square

# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 1

        def magic(r, c, v):
            Sum = sum(grid[r][c : c + v])

            for i in range(r, r + v):
                if sum(grid[i][c : c + v]) != Sum:
                    return False
            
            for i in range(c, c + v):
                col = 0
                for j in range(r, r + v):
                    col += grid[j][i]
                if col != Sum:
                    return False
            
            d1 = 0
            for i in range(v):
                d1 += grid[r + i][c + i]
            if d1 != Sum:
                return False
            
            d2 = 0
            for i in range(v):
                d2 += grid[r + i][c + v - i - 1]
            if d2 != Sum:
                return False
            
            return True

        for r in range(m):
            for c in range(n):
                for v in range(2, min(m - r, n - c) + 1):
                    if magic(r, c, v):
                        res = max(res, v)
        return res