# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# original

class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) < 2:
                return i
        