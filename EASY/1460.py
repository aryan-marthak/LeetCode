# 1460. Make Two Arrays Equal by Reversing Subarrays

# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

# Return true if you can make arr equal to target or false otherwise.

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
    
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        for n1, n2 in zip(target, arr):
            count[n1] += 1
            count[n2] -= 1
        for n in count:
            if count[n] != 0:
                return False
        return True