# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# BACKTRACKING
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(Open, close, string):
            if Open == n and close == n:
                res.append(string)
                return
            if Open < n:
                backtrack(Open + 1, close, string + "(")
            if close < Open:
                backtrack(Open, close + 1, string + ")")
        backtrack(0, 0, "")         
        return res