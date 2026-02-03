# 3637. Trionic Array I

# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

#     nums[0...p] is strictly increasing,
#     nums[p...q] is strictly decreasing,
#     nums[q...n − 1] is strictly increasing.

# Return true if nums is trionic, otherwise return false.

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i = 1
        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == len(nums):
            return False
        while i < len(nums) and nums[i] < nums[i - 1]:
            i += 1
        if i == len(nums):
            return False
        while i < len(nums) and nums[i] > nums[i - 1]:
            i += 1
        return i == len(nums)