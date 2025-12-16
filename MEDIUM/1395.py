# 1395. Count Number of Teams

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

#     Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
#     A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# RECURSION WITH MEMOIZATION (TOP-DOWN DP)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cache = {}
        def backtrack(i, ascend, count):
            if (i, ascend, count) in cache:
                return cache[(i, ascend, count)]
            if count == 3:
                return 1
            if i == len(rating):
                return 0
            res = 0
            for j in range(i + 1, len(rating)):
                if ascend and rating[i] < rating[j]:
                    res += backtrack(j, ascend, count + 1)
                if not ascend and rating[i] > rating[j]:
                    res += backtrack(j, ascend, count + 1)
            cache[(i, ascend, count)] = res
            return res
        res = 0
        for i in range(len(rating)):
            res += backtrack(i, True, 1)
            res += backtrack(i, False, 1)
        return res
    
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            Sum = nums[i] if even else -nums[i]
            dp[(i, even)] = max(Sum + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]
        return dfs(0, True)