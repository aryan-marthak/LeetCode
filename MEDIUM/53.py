# 53. Maximum Subarray

# Given an integer array nums, find the
# subarray
# with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # KADANE's ALGO

        sum = 0
        maxi = float('-inf')

        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0

        return maxi
        
        # maxi = min(nums)
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         maxi = max(maxi, total)
        # return maxi