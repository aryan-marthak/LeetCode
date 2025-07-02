# 2696. Minimum String Length After Removing Substrings

# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            stack.append(c)

            if (len(stack) >= 2 and ((stack[-2] == "A" and stack[-1] == "B") or (stack[-2] == "C" and stack[-1] == "D"))):
                stack.pop()
                stack.pop()
        return len(stack)
                
        # stack = []
        # for c in s:
        #     if not stack:
        #         stack.append(c)
        #         continue
        #     if c == "B" and stack[-1] == "A":
        #         stack.pop()
        #     elif c == "D" and stack[-1] == "C":
        #         stack.pop()
        #     else:
        #         stack.append(c)
        # return len(stack)