# 78. Subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# ITERATIVE APPROACH

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            temp = []
            for j in res:
                temp.append(j + [i])
            res.extend(temp)
        return res