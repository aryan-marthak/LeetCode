# 300. Longest Increasing Subsequence

# Given an integer array nums, return the length of the longest strictly increasing subsequence.
                    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        res = 1
        for i in nums[1:]:
            if i > temp[-1]:
                temp.append(i)
                res += 1
            else:
                l, r = 0, len(temp) - 1
                while l < r:
                    mid = (l + r) // 2
                    if temp[mid] < i:
                        l = mid + 1
                    else:
                        r = mid
                temp[l] = i
        return res

        # Time complexity: O(n log n)
        # Space complexity: O(n)

        # temp = [nums[0]]
        # res = 1
        # for i in nums[1:]:
        #     if i > temp[-1]:
        #         temp.append(i)
        #         res += 1
        #     else:
        #         x = 0
        #         while x < len(temp) and temp[x] < i:
        #             x += 1
        #         temp[x] = i
        # return res

        # Time complexity: O(n^2)
        # Space complexity: O(n)