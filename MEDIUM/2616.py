# 2616. Minimize the Maximum Difference of Pairs

# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def can_distribute(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n

        l, r = 1, max(quantities)
        res = 0
        while l <= r:
            x = (l + r) // 2
            if can_distributive(x):
                res = x
                r = x - l
            else:
                l = x + 1
        return res