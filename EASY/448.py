# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        result = []
        for i in range(1, len(nums) + 1):
            if i not in freq_map:
                result.append(i)

        return result