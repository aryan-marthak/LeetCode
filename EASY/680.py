# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r):
            left, right = l, r
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right - 1)
            left += 1
            right -= 1
        return True