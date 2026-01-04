# 1390. Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# OPTIMAL SOLUTION DIVISIOR PAIRING
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        Sum = 0
        for i in nums:
            temp = 0
            curr = 0
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    temp += 1
                    curr += j
                    if j != i // j:
                        temp += 1
                        curr += i // j
                if temp > 4:
                    break             
            if temp == 4:
                Sum += curr
        return Sum

# BRUTE FORCE SOLUTION
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        Sum = 0
        for i in nums:
            temp = 0
            curr = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    temp += 1
                    curr += j
            if temp == 4:
                Sum += curr
        return Sum