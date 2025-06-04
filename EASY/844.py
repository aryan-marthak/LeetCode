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
    
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getValid(string, index):
            back = 0
            while index >= 0:
                if string[index] == "#":
                    back += 1
                elif back > 0:
                    back -= 1
                else:
                    return index
                index -= 1
            return -1
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = getValid(s, i)
            j = getValid(t, j)
            
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True