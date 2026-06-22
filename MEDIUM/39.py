# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, current_sum, index):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(path, current_sum +  candidates[i], i)
                path.pop()
        backtrack([], 0, 0)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(start, curr, target):
            if target == 0:
                res.append(curr)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                comb(i, curr + [candidates[i]], target - candidates[i])
            return        
        comb(0, [], target)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, temp, Sum):
            if Sum == target:
                res.append(temp.copy())
                return
            if i >= len(candidates) or Sum > target:
                return
            temp.append(candidates[i])
            backtrack(i, temp, Sum + candidates[i])
            temp.pop()
            backtrack(i + 1, temp, Sum)
        backtrack(0, [], 0)
        return res