# 678. Valid Parenthesis String

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# RECURSION WITH BACKTRACKING
class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == '(':
                return dfs(i + 1, open + 1)
            elif s[i] == ')':
                return dfs(i + 1, open - 1)
            else:
                return (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
        return dfs(0, 0)

# MEMOIZATION TOP-DOWN DP
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, open):
            if open < 0:
                return False
            if (i, open) in dp:
                return dp[(i, open)]
            if i == len(s):
                return open == 0
            if s[i] == '(':
                res = dfs(i + 1, open + 1)
            elif s[i] == ')':
                res = dfs(i + 1, open - 1)
            else:
                res = (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
            dp[(i, open)] = res
            return res
        return dfs(0, 0)
    
# STACK
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left
    
# GREEDY
class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0 
        maxOpen = 0

        for c in s:
            if c == "(":
                minOpen += 1
                maxOpen += 1

            elif c == ")":
                minOpen -= 1
                maxOpen -= 1

            else:  # '*'
                minOpen -= 1    
                maxOpen += 1  

            if maxOpen < 0:
                return False

            if minOpen < 0:
                minOpen = 0
        return minOpen == 0