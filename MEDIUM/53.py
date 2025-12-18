# 53. Maximum Subarray

# Given an integer array nums, find the
# subarray
# with the largest sum, and return its sum.

# BRUTE FORCE - O(N^2) TIME
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                res = max(res, temp)
        return res
    
# BRUTE FORCE - ALTERNATE
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = min(nums)
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                maxi = max(maxi, total)
        return maxi

# OPTIMIZED - O(N) TIME # KADANE's ALGO
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = float('-inf')

        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0

        return maxi
