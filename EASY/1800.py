# 1800. Maximum Ascending Subarray Sum

# Given an array of positive integers nums, return the maximum possible sum of an in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# Brute force solution
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                cur += nums[j]
            res = max(res, cur)
        return res
# Time complexity: O(n^2)
# Space complexity: O(1)

# Optimized solution
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cur = 0
            cur += nums[i]
            res = max(res, cur)
        return res
# Time complexity: O(n)
# Space complexity: O(1)