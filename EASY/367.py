# 367. Valid Perfect Square

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# not the best
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num**0.5
        if x == int(x):
            return True
        else: 
            return False
        
# brute force approach (TLE ERROR)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # brute force approach

        for i in range(1, num + 1):
            if i * i == num:
                return True
        return False