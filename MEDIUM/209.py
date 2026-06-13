# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Brute Force (TLE)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        for i in range(len(nums)):
            Sum = 0
            for j in range(i, len(nums)):
                Sum += nums[j]
                if Sum >= target:
                    res = min(res, j - i + 1)
                    break
        return 0 if res == float('inf') else res

# OPTIMIZED Approach (sliding window)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, temp = 0, 0

        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                res = min(res, r - l + 1)
                temp -= nums[l]
                l += 1
        return 0 if res == float('inf') else res

