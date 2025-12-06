# 1048. Longest String Chain

# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

#     For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: -len(w))
        lst = {}
        for i, j in enumerate(words):
            lst[j] = i

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1
            for j in range(len(words[i])):
                w = words[i]
                pred = w[:j] + w[j+1:]
                if pred in lst  :
                    res = max(res, 1 + dfs(lst[pred]))
                dp[i] = res
            return res
        for i in range(len(words)):
            dfs(i)
        return max(dp.values())