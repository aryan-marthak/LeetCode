# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):    
            for i in range(1, len(nums)):
                if i == 1:
                    nums[i] = max(nums[i], nums[i - 1])
                else:
                    nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            return nums[-1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))