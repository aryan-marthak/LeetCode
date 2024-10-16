# 1. TWO SUM 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): 
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

nums = [1,2,3,4,5]
target = 4

result = twoSum(nums, target)
print(result) 