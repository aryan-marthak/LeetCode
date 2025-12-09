# 516. Longest Palindromic Subsequence

# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            if l == r:
                return 1
            if s[l] == s[r]:
                dp[(l, r)] = 2 + dfs(l + 1, r - 1)
            else:
                dp[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            return dp[(l, r)]
        return dfs(0, len(s) - 1)