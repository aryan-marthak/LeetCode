# 540. Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# BRUTE FORCE O(n)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if ((i and nums[i] == nums[i - 1]) or
                (i < n - 1 and nums[i] == nums[i + 1])
            ):
                continue
            return nums[i]
        
# BINARY SEARCH

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and 
                (m + 1 == len(nums) or nums[m + 1] != nums[m])):
                return nums[m]
            lsize = m - 1 if nums[m - 1] == nums[m] else m
            if lsize % 2:
                r = m - 1
            else: 
                l = m + 1