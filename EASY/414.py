# 414. Third Maximum Number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = max(nums)
        for i in range(3):
            if len(nums) > 0:
                max_num = max(nums)
                nums.remove(max_num)
            else:
                return maximum
        return max_num