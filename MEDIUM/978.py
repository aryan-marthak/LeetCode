# 978. Longest Turbulent Subarray

# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

#     For i <= k < j:
#         arr[k] > arr[k + 1] when k is odd, and
#         arr[k] < arr[k + 1] when k is even.
#     Or, for i <= k < j:
#         arr[k] > arr[k + 1] when k is even, and
#         arr[k] < arr[k + 1] when k is odd.

# TWO POINTERS SLIDING WINDOW
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res