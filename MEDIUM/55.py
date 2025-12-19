# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Dynamic Programming - Bottom-Up Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            end = min(len(nums), i + nums[i])
            for j in range(i + 1, end + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

# Reccursion with Memoization (Top-Down DP)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return True
            end = min(len(nums) - 1, nums[i] + i)
            for j in range(i + 1, end + 1):
                if dfs(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(0)

# Reccursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) - 1:
                return True
            end = min(len(nums) - 1, nums[i] + i)
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False
        return dfs(0)

# Greedy Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0