# 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2)
            res *= res
            return x * res if n % 2 else res
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

# WRONG SOLUTION (MAX RECURSION DEPTH EXCEEDED)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         if n < 0:
#             x = 1/x
#             n = -n
#         if n > 0:
#             temp = self.myPow(x, n - 1)
#             return temp * x