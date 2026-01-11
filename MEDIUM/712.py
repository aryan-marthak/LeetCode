# 712. Minimum ASCII Delete Sum for Two Strings

# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

# BOTTOM UP DP
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )
        return dp[0][0]

# TOP DOWN DP WITH MEMOIZATION
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = {} 
        def dfs(i,j):
            if i == m: 
                return sum([ord(c) for c in s2[j:]])
            if j == n: 
                return sum([ord(c) for c in s1[i:]])
            if (i, j) in dp:
                return dp[(i, j)] 
            if s1[i] == s2[j]:
                dp[(i, j)] = dfs(i+1,j+1)
            else:  
                dp[(i, j)] = min(ord(s1[i])+dfs(i+1,j),ord(s2[j])+dfs(i,j+1))
            return dp[(i, j)]
        return dfs(0,0)