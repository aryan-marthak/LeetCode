# 1458. Max Dot Product of Two Subsequences

# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}

        # max dot product of two subsequences starting at i,j
        def dp(i,j):

            if i == len(nums1) or j == len(nums2):
                return float("-inf") # if we are passed the boundary, dont pick anything from there.

            if (i,j) in memo:
                return memo[(i,j)]

            take = nums1[i] * nums2[j]
            res = max(
            # take i,j. move forward
                take + dp(i+1, j+1),

            # take this subsequence and just end.
                take,

            # skip i: i+1,j
                dp(i+1,j),

            # skip j: i,j+1
                dp(i,j+1),
            )

            memo[(i,j)] = res

            return memo[(i,j)]

        return dp(0,0)