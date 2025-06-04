# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                r -= 1
        return nums