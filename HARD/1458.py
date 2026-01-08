# 1458. Max Dot Product of Two Subsequences

# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

# BOTTOM UP DP


# TOP DOWN DP WITH MEMOIZATION
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            if (i, j) in dp:
                return dp[(i, j)]
            dot = nums1[i] * nums2[j]
            res = max(dot, dot + dfs(i + 1, j + 1), dfs(i, j + 1), dfs(i + 1, j))
            dp[(i, j)] = res
            return dp[(i, j)]
        return dfs(0, 0)