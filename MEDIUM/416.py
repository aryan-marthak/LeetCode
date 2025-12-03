# 416. Partition Equal Subset Sum

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        subsets = [[]]
        for i in nums:
            temp = []
            for j in subsets:
                temp.append(j + [i])
            for k in temp:
                subsets.append(k)
        for i in subsets:
            if sum(i) == target:
                return True
        return False
    
