# 459. Repeated Substring Pattern

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        subs = ''
        for i in range(len(s) // 2):
            subs += s[i]
            if len(s) % len(subs) == 0:
                if subs * (len(s) // len(subs)) == s:
                    return True
        return False

    #     class Solution:
    #         def repeatedSubstringPattern(self, s: str) -> bool:
    #             n = len(s)
    #             for i in range(1, n//2 + 1):
    #                 if n % i == 0:
    #                     substring = s[:i]
    #                     if substring * (n // i) == s:
    #                         return True
    #             return False