# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        res = {}
    
        for i in range(len(nums)):
            if nums[i] in res:
                if i - res[nums[i]] <= k:
                    return True
            res[nums[i]] = i
        return False