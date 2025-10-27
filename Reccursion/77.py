# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(x, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(x, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res