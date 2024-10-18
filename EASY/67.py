# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
    def addBinary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        z = bin(x + y)
        z = z.replace("0b", "")
        return z