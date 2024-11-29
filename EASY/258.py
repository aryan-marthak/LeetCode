# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# ITERATIVE APPROACH O(log(n))

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0 
        while num > 9:
            while num:
                sum += (num % 10)
                num //= 10
            num = sum
            sum = 0
        return num
    
# MATHEMATICAL LOGIC O(n)

 