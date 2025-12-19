# 1749. Maximum Absolute Sum of Any Subarray

# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

#     If x is a negative integer, then abs(x) = -x.
#     If x is a non-negative integer, then abs(x) = x.

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minpre, maxpre = 0, 0
        cur = 0
        res = 0

        for i in nums:
            cur += i
            res = max(res, abs(cur - minpre), abs(cur - maxpre))
            minpre = min(minpre, cur)
            maxpre = max(maxpre, cur)
        return res