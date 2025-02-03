# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = [0] * len(nums)
        k = k % len(nums)
        for i in range(len(nums)):
            temp[(i+k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]