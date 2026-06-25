# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        count ={}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res

# Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                count = 1
                candidate = n
            elif candidate == n:
                count += 1
            else:
                count -= 1
        
        temp = nums.count(candidate)
        if temp > len(nums) // 2:
            return candidate