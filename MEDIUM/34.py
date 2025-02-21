# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l  
        
        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left = findLeft(nums, target)
        right = findRight(nums, target)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]