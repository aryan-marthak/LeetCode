# 482. License Key Formatting

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-", "")
        count = k
        ret = ""
        s = s[::-1]
        for i, j in enumerate(s):
            ret += j
            count -= 1
            if count == 0 and i != len(s) - 1:
                ret += "-"
                count = k
        ret = ret[::-1]
        return ret