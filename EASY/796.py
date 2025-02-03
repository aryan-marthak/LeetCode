# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

#     For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        list_s = list(s)
        for i in range(len(s)):
            x = list_s.pop()
            list_s.insert(0, x)
            s = "".join(list_s)
            if s == goal:
                return True
        return False

        # if len(goal) != len(s):
        #     return False
        # s += s
        # return goal in s