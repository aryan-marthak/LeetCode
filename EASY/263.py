# 263. Ugly Number

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2 
            elif n % 3 == 0:
                n /= 3 
            elif n % 5 == 0:
                n /= 5
            else:
                break
        if n == 1:
            return True
        else:
            return False
        