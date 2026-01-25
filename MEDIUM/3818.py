# 3818. Minimum Prefix Removal to Make Array Strictly Increasing

# You are given an integer array nums.

# You need to remove exactly one prefix (possibly empty) from nums.

# Return an integer denoting the minimum length of the removed
# such that the remaining array is .

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                return i
        return 0