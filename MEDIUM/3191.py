# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

# You are given a nums.

# You can do the following operation on the array any number of times (possibly zero):

#     Choose any 3 consecutive elements from the array and flip all of them.

# Flipping an element means changing its value from 0 to 1, and from 1 to 0.

# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] == 1
                nums[i + 1] = 0 if nums[i + 1] == 1 else 1
                nums[i + 2] = 0 if nums[i + 2] == 1 else 1
                res += 1
        if not nums[-1] or not nums[-2]:
            return -1
        return res