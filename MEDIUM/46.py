# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, nums):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(path + [nums[i]], nums[:i] + nums[i+1:])
        backtrack([], nums)
        return res