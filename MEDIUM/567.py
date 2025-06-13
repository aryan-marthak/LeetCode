# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a

# of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# BRUTE FORCE Approach

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False