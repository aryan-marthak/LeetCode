# 3174. Clear Digits

# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

#     Delete the first digit and the closest non-digit character to its left.

# Return the resulting string after removing all digits.

# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            if c.isnumeric():
                stack.pop()
                stack.pop()
        return "".join(stack)