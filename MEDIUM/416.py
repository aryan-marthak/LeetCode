# 416. Partition Equal Subset Sum

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# BRUTE FORCE APPROACH
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
    
# DP APPROACH
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            newdp = set()
            for j in dp:
                newdp.add(j + nums[i])
                newdp.add(j)
            dp = newdp
        return True if target in dp else False