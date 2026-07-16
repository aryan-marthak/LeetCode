# 1624. Largest Substring Between Two Equal Characters

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

# Brute force solution
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            for j in range(1, len(s)):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
        return res
# Time complexity: O(n^2)
# Space complexity: O(1)

# Optimized solution
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        Map = {}
        res = -1

        for i, v in enumerate(s):
            if v in Map:
                res = max(res, i - Map[v] - 1)
            else:
                Map[v] = i
        return res
# Time complexity: O(n)
# Space complexity: O(n)