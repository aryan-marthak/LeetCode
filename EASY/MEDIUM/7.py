# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        rev = 0
        sgn = 1
        if x == 0:
            return 0
        if x < 0:
            sgn = -1
        while abs(x)>0:
            digit = abs(x) % 10
            rev = (rev * 10) + digit
            x = abs(x) / 10
        if rev < -2147483648 or rev > 2147483647:
            return 0
        else:
            return rev * sgn


# EASY AND READABLE APPROACH

class Solution:
    def reverse(self, x: int) -> int: 
        s = str(abs(x))      
        reversed = int(s[::-1])

        if reversed > 2147483647:
            return 0
        return reversed if x > 0 else (reversed * -1)