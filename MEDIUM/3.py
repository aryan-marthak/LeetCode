# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest
# without duplicate characters.

# SLIDING WINDOW Approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1
            Set.add(s[r])
            res = max(res, r - l + 1)
        return res

# BRUTE FORCE Approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            Set = set()
            for j in range(i, len(s)):
                if s[j] in Set:
                    break
                Set.add(s[j])
            res = max(res, len(Set))
        return res