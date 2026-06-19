# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# OPTIMAL SOLUTION O(log(m * n)) time complexity
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

# O(log(m * n)) time complexity
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

# O(m + n) time complexity
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False

# O(m * n) time complexity
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in matrix:
            for j in i:
                res.append(j)
        l, r = 0, len(res) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if res[m] == target:
                return True
            elif res[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False