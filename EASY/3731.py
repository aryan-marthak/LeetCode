# 3731. Find Missing Elements

# You are given an integer array nums consisting of unique integers.

# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

# The smallest and largest integers of the original range are still present in nums.

# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        res = []
        for i in range(mini, maxi+1):
            if i not in nums:
                res.append(i)
        return res