# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Brute Force
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res =  0
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                if temp == k:
                    res += 1
        return res

# Prefix Sum OPTIMAL
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dict = defaultdict(int)
        Sum = 0
        res = 0
        Dict[0] = 1
        for i in nums:
            Sum += i
            res += Dict[Sum - k]
            Dict[Sum] += 1
        return res