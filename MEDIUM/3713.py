# 3713. Longest Balanced Substring I

# You are given a string s consisting of lowercase English letters. A of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

class Solution:
    def longestBalanced(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            Dict = defaultdict(int)
            for j in range(i, len(s)):
                Dict[s[j]] += 1

                vals = Dict.values()
                if len(set(vals)) == 1:
                    maxlen = max(maxlen, j - i + 1)
        return maxlen