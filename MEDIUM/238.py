# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Product of Prefix and Suffix OPTIMAL O(1) Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Prefix and Suffix Product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lmult = 1
        rmult = 1
        larr = [0] * len(nums)
        rarr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i -1 
            larr[i] = lmult
            rarr[j] = rmult
            lmult *= nums[i]
            rmult *= nums[j]
        
        return[l*r for l, r in zip(larr, rarr)]

# Brute Force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp *= nums[j]
            ans.append(temp)
        return ans