# 3719. Longest Balanced Subarray I

# You are given an integer array nums. A is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

# Return the length of the longest balanced subarray.

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxlen = 0
        for i in range(len(nums)):
            check = set()
            e, o = 0, 0
            for j in range(i, len(nums)):
                if nums[j] not in check:
                    if nums[j] % 2 == 0:
                        e += 1
                    else:
                        o += 1
                    check.add(nums[j])
                
                if o == e:
                    maxlen = max(maxlen, j - i + 1)
        return maxlen