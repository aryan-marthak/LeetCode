# 474. Ones and Zeroes

# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            zeros, ones = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if zeros <= m and ones <= n:
                dp[(i, m, n)] = max(dfs(i + 1, m, n), 1 + dfs(i + 1, m - zeros, n - ones))
            return dp[(i, m, n)]
        return dfs(0, m, n)