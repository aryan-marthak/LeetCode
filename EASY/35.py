# 35. Search Inserted Position 

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        start, end = 0, (len(nums)) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end -= 1
            else:
                start += 1
        return start