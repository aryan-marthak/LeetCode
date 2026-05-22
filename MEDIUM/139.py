# 139. Word Break

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BOTTOM UP DP
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
    
        # TOP DOWN DP
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)