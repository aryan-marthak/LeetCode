# 3314. Construct the Minimum Bitwise Array I

# You are given an array nums consisting of n

# integers.

# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].

# Additionally, you must minimize each value of ans[i] in the resulting array.

# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums:
            k = 0
            temp = p
            while temp & 1:
                k += 1
                temp >>= 1
            if k == 0:
                ans.append(-1)
            else:
                ans.append(p - (1 << (k - 1)))
        return ans

# Brute Force Approach
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            x = -1
            for j in range(1, i):
                if j | (j + 1) == i:
                    x = j
                    break
            res.append(x) 
        return res