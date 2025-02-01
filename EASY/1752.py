# 1752. Check if Array Is Sorted and Rotated

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
        if nums[-1] > nums[0]:
            count += 1
        return count <= 1