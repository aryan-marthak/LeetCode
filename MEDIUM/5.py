# 5. Longest Palindromic Substring

# Given a string s, return the longest in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
        
        # res, resLen = "", 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1

        #         if l >= r and resLen < (j - i + 1):
        #             res = s[i : j + 1]
        #             resLen = j - i + 1
        # return res