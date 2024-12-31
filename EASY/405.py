# 405. Convert a Number to Hexadecimal

# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) -> str:
        output = []
        Map = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        while num > 0:
            digit = num % 16
            num //= 16
            if digit > 9 and digit < 16:
                digit = Map[digit]
            else:
                digit = str(digit)
            output.append(digit)
        return "".join(output[::-1])