# 191. Number of 1 Bits

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

class Solution(object):
    def hammingWeight(self, n):
        x = ""
        res = 0

        while n > 0:
            if n % 2 == 0:
                x += "0"
            else:
                x += "1"
            n = n // 2
        for i in x:
            if i == "1":
                res += 1
        return res