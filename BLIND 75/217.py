# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] > 1:
                return True
        return False

        # count = defaultdict()
        # for i in nums:
        #     count[i] += 1
        #     if count[i] > 1:
        #         return True
        # return False


        # Set = set(nums)
        # return len(nums) != len(Set)