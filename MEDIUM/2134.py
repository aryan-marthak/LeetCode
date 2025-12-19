# 2134. Minimum Swaps to Group All 1's Together II

# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = nums.count(1)
        l = 0
        cur_ones = max_ones = 0
        for i in range(2 * len(nums)):
            if nums[i % len(nums)]:
                cur_ones += 1
            if i - l + 1 > total:
                cur_ones -= nums[l % len(nums)]
                l += 1
            max_ones = max(max_ones, cur_ones)
        return total - max_ones