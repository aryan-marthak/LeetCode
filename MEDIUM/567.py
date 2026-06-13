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
    
# OPTIMIZED Approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)):
            if sorted(s2[i:i + len(s1)]) == s1:
                return True
        return False
    
# OPTIMIZED Approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            if sorted(s2[i:i + len(s1)]) == s1:
                return True
        return False

# OTIMIMAL Approach (sliding window)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = [0] * 26
        c2 = [0] * 26
        
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1

        if c1 == c2:
            return True

        for i in range(len(s1), len(s2)):
            c2[ord(s2[i]) - ord('a')] += 1
            c2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if c1 == c2:
                return True
        return False