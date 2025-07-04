# 962. Maximum Width Ramp

# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.






# BRUTE FORCE TWO POINTER

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        diff = 0
        width = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] <= nums[j]:
                    width = j - i
                diff = max(diff, width)
        return diff