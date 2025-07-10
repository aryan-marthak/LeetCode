# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

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