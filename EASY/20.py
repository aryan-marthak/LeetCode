# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack 
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"(" : ")", "{" : "}", "[" : "]"}

        for c in s:
            if c in dictionary:
                stack.append(c)
            elif not stack or dictionary[stack.pop()] != c:
                return False
        return not stack