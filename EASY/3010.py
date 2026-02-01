# 3010. Divide an Array Into Subarrays With Minimum Cost I

# You are given an array of integers nums of length n.

# The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

# You need to divide nums into 3 disjoint contiguous

# .

# Return the minimum possible sum of the cost of these subarrays.

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        min1 = float('inf')
        min2 = float('inf')
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < min1:
                min2 = min1
                min1 = curr
            elif curr < min2:
                min2 = curr
        res += min1
        res += min2
        return res