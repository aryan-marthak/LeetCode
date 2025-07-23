# 1394. Find Lucky Integer in an Array

# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # COUNTER
        
        from collections import Counter

        freq = Counter(arr)
        temp = -1

        for i, j in freq.items():
            if i == j:
                temp = max(temp, i)
        return temp

        # BRUTE FORCE APPROACH

        comp = -1
        for i in arr:
            temp = i
            res = 0
            for j in arr:
                if j == temp:
                    res += 1
            if res == temp:
                comp = max(comp, temp)
        return comp

