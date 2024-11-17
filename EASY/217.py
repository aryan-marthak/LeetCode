# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        res = set()

        for i in nums:
            if i in res:
                return True
            res.add(i)
        return False