# 415. Add Strings

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0:
            val_i = int(num1[i]) if i >= 0 else 0
            val_j = int(num2[j]) if j >= 0 else 0

            Sum = val_i + val_j + carry
            res.append(str(Sum % 10))

            carry = Sum // 10

            i -= 1
            j -= 1

        if carry:
            res.append(str(carry))
        return "".join(reversed(res))
