# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        s = set(nums)
        for i in range(x+1):
            if i not in s:
                return i