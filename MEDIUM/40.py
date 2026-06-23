# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb(curr, start, target):
            if target == 0:
                res.append(curr)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                comb(curr + [candidates[i]], i + 1, target-candidates[i])
            return
        comb([], 0, target)
        return res

# Time Complexity: O(2^n) where n is the number of candidates. In the worst case, we might explore all possible combinations of candidates.
# Space Complexity: O(k) where k is the maximum depth of the recursion tree, which can be at most n in the worst case. Additionally, we use space to store the result combinations, which can also take up to O(2^n) in the worst case.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def bt(i, curr, Sum):
            if Sum == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or Sum > target:
                return
            curr.append(candidates[i])
            bt(i + 1, curr, Sum + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i + 1, curr, Sum)
        bt(0, [], 0)
        return res

# Time Complexity: O(2^n) where n is the number of candidates. In the worst case, we might explore all possible combinations of candidates.
# Space Complexity: O(k) where k is the maximum depth of the recursion tree, which can be at most n in the worst case. Additionally, we use space to store the result combinations, which can also take up to O(2^n) in the worst case.