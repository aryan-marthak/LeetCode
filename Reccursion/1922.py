# 1922. Count Good Numbers

# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

#     For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

# MODULAR EXPONENTIATION

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(a, b):
            result = 1
            a = a % MOD
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return result

        total_even = (n + 1) // 2
        total_odd = n // 2
        return (mod_pow(5, total_even) * mod_pow(4, total_odd)) % MOD

# TLE SOLUTION
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        total_even = (n + 1) // 2
        total_odd = n // 2

        even_count = (5 ** total_even) % ((10 ** 9) + 7)
        odd_count = (4 ** total_odd) % ((10 ** 9) + 7)

        total = (even_count * odd_count) % ((10 ** 9) + 7)

        return total