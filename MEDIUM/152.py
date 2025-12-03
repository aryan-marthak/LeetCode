# 152. Maximum Product Subarray

# Given an integer array nums, find a

# that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Brute Force Approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res

# Dynamic Programming Approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            res = max(res, curMax)
        return res