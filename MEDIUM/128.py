# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# HashSet
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        res = 0

        for i in Set:
            if (i - 1) not in Set:
                curr = 1
                while i + curr in Set:
                    curr += 1
                res = max(res, curr)
        return res

# Sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()
        streak, curr, i = 0, nums[0], 0
        while i < len(nums):
            if curr != nums[i]:
                streak = 0
                curr = nums[i]
            while i < len(nums) and curr == nums[i]:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res

# Brute Force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            res = 0
            Set = set(nums)

            for i in nums:
                streak = 0
                curr = i
                while curr in Set:
                    curr += 1
                    streak += 1
                res = max(res, streak)
            return res