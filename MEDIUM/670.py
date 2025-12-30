# 670. Maximum Swap

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.



# BRUTE FORCE
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        value = num

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                value = max(value, int("".join(nums)))
                nums[i], nums[j] = nums[j], nums[i]
        return value