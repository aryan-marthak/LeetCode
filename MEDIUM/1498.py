# 1498. Number of Subsequences That Satisfy the Given Sum Condition

# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1000000007

        nums.sort()
        res = 0
        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r-i))
                res %= MOD
        return res

        # def dfs(maxi, mini, i):
        #     if i == len(nums):
        #         if mini != float("inf") and (maxi + mini) <= target:
        #             return 1
        #         return 0

        #     skip = dfs(maxi, mini, i + 1)
        #     include = dfs(max(maxi, nums[i]), min(mini, nums[i]), i + 1)
        #     return (skip + include) % MOD

        # return dfs(float("-inf"), float("inf"), 0)