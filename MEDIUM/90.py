# 90. Subsets II

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        last = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                start = last
            else:
                start = 0
            last = len(res)
            for j in range(start, len(res)):
                res.append(res[j] + [nums[i]])
        return res