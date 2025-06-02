# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


# recursion way

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        fs = []
        for i in s:
            if i.isalnum():
                fs.append(i)
        def helper(l = 0, r = None):
            if r is None:
                r = len(fs) - 1
            if l >= r:
                return True
            if fs[l] != fs[r]:
                return False
            return helper(l + 1, r - 1)
        return helper()
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and s[l].isalnum() == False:
                l += 1        
            while r > l and s[r].isalnum() == False:
                r -= 1        
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True