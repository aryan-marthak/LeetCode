# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

# You are given an array of integers nums. Return the length of the longest of nums which is either strictly increasing or strictly decreasing.

# Brute force solution
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        resi = 1
        resd = 1

        temp = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                temp = 1
            else:
                temp += 1
            resi = max(temp, resi)
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                temp = 1
            else:
                temp += 1
            resd = max(temp, resd)

        return max(resi, resd)
# Time complexity: O(n)
# Space complexity: O(1)