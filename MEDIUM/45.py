# 45. Jump Game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

#     0 <= j <= nums[i] and
#     i + j < n

# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            end = min(len(nums) - 1, i + nums[i])
            res = float('inf')
            for j in range(i + 1, end + 1):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return res
        return dfs(0)