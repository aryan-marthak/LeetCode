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
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            bt(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, curr)
        bt(0, [])
        return res
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = {()}

        for i in nums:
            temp = []
            for j in res:
                temp.append(j + (i,))
            res.update(temp)
        return[list(i) for i in res]