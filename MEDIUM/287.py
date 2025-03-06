# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for i, j in nums.items():
            if j > 1:
                return i