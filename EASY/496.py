# 496. Next Greater Element I

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Brute force solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            for a, b in enumerate(nums2):
                if b == i:
                    temp = b
                    for x in range(a + 1, len(nums2)):
                        if nums2[x] > temp:
                            res.append(nums2[x])
                            break
                    else:
                        res.append(-1)
        return res         
# Time complexity: O(n^2)
# Space complexity: O(n)