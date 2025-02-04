# 1021. Remove Outermost Parentheses

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

#     For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

class Solution(object):
    def removeOuterParentheses(self, s):
        # res = ""
        # temp = 0
        # for i in s:
        #     if i == "(":
        #         if temp > 0:
        #             res += i
        #         temp += 1
        #     else:
        #         temp -= 1
        #         if temp > 0:
        #             res += i
        # return res

        stack = []
        res = ""
        for i in s:
            if i == "(":
                if stack:
                    res += i
                stack.append(i)

            elif i == ")":
                stack.pop()
                if stack:
                    res += i

        return res