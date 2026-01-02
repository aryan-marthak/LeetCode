# 961. N-Repeated Element in Size 2N Array

# You are given an integer array nums with the following properties:

#     nums.length == 2 * n.
#     nums contains n + 1 unique elements.
#     Exactly one element of nums is repeated n times.

# Return the element that is repeated n times.

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in nums:
            if len(nums) == 2 * nums.count(i) and len(set(nums)) == nums.count(i) + 1:
                return i