# 740. Delete and Earn

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

#     Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

# Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curr = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curr + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curr + earn2
                earn1 = temp
        return earn2 