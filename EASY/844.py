# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(a):
            temp = []
            for i in a:
                if i != "#":
                    temp.append(i)
                elif temp:
                    temp.pop()
            return temp
        return check(s) == check(t)