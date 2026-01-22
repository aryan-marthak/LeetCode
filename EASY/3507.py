# 3507. Minimum Pair Removal to Sort Array I

# Given an array nums, you can perform the following operation any number of times:

#     Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
#     Replace the pair with their sum.

# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def helper(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        res = 0
        while not helper(nums):
            Sum = float('inf')
            merge = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < Sum:
                    Sum = nums[i] + nums[i + 1]
                    merge = i
            nums[merge] += nums[merge + 1]
            nums.pop(merge + 1)
            res += 1
        return res
