# 1911. Maximum Alternating Subsequence Sum

# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

#     For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.

# Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            Sum = nums[i] if even else -nums[i]
            dp[(i, even)] = max(Sum + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]
        return dfs(0, True)