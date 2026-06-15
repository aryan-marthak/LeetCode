# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Brute Force (TLE)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)

        ans = ""
    
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
    
                if Counter(sub) >= need:
                    if ans == "" or len(sub) < len(ans):
                        ans = sub
    
        return ans

# OPTIMIZED Approach (sliding window)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = Counter(t)
        formed, total = 0, len(d)
        l = r = 0
        lenans = float('inf')
        subl, subr = 0, 0

        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1
            while l <= r and formed == total:
                currlen = r - l + 1
                if currlen < lenans:
                    lenans = currlen
                    subl, subr = l, r + 1
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if lenans == float('inf') else s[subl:subr]