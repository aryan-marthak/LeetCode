# 3442. Maximum Difference Between Even and Odd Frequency I

# You are given a string s consisting of lowercase English letters.

# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

#     a1 has an odd frequency in the string.
#     a2 has an even frequency in the string.

# Return this maximum difference.

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        res = float("-inf")

        for i in count.values():
            if i % 2 == 0: continue
            for j in count.values():
                if j % 2 == 1: continue
                res = max(res, i - j)

        return res