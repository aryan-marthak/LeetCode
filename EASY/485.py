# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] == 1:
                nums[i] += nums[i-1]
        return max(nums)