# 2149. Rearrange Array Elements by Sign

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

#     Every consecutive pair of integers have opposite signs.
#     For all integers with the same sign, the order in which they were present in nums is preserved.
#     The rearranged array begins with a positive integer.

# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in nums:
            if i > 0:
                pos.append[i]
            else:
                neg.append[i]
        x = 0
        while 2 * x < len(nums):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
            i += 1
        return nums
