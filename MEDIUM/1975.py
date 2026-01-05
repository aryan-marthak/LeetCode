# 1975. Maximum Matrix Sum

# You are given an n x n integer matrix. You can do the following operation any number of times:

#     Choose any two adjacent elements of matrix and multiply each of them by -1.

# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        Sum = 0
        neg_count = 0
        Min = float('inf')
        for i in matrix:
            for j in i:
                if j < 0:
                    neg_count += 1
                abs_j = abs(j)
                Sum += abs_j
                Min = min(Min, abs_j)
        if neg_count % 2 == 1:
            Sum -= 2 * Min
        return Sum