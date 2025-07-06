# 456. 132 Pattern

# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# BRUTE FORCE APPROACH

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for k in range(2, len(nums)):
            for j in range(k - 1, 0, -1):
                if nums[j] <= nums[k]:
                    continue
                for i in range(j - 1, -1, -1):
                    if nums[i] < nums[k]:
                        return True
        return False 
    
# 