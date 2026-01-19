# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

# Brute Force Approach
class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        ans = 0

        for k in range(1, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    s = 0
                    for x in range(i, i + k):
                        for y in range(j, j + k):
                            s += mat[x][y]
                    if s <= threshold:
                        ans = max(ans, k)

        return ans
