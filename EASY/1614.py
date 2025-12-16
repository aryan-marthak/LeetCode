# 1614. Maximum Nesting Depth of the Parentheses

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# ITERATIVE
class Solution:
    def maxDepth(self, s: str) -> int:
        final = current = 0

        for i in s:
            if i == "(":
                current += 1
            elif i == ")":
                current -= 1
            final = max(final, current)
        return final