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