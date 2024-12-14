# 9. Palindrome Number 
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        return(bool(str(num)[::-1] == num))
    

class Solution(object):
    def isPalindrome(self, x):
        s = str(abs(x))
        reversed = int(s[::-1])
        return reversed == x if x >= 0 else False