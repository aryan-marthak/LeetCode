# 504. Base 7

# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        og = num
        num = abs(num)
        remainders = []

        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7

        if og < 0:
            remainders.append("-")
        remainders.reverse()
        return ''.join(remainders)