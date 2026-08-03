# 2437. Number of Valid Clock Times

# You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

# In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

# Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

class Solution:
    def countTime(self, time: str) -> int:
        a, b, c, d, e = time

        if a == "?" and b == "?":
            res1 = 24
        elif a == "?":
            if int(b) <= 3:
                res1 = 3
            else:
                res1 = 2
        elif b == "?":
            if int(a) == 2:
                res1 = 4
            else:
                res1 = 10
        else:
            res1 = 1

        if d == '?' and e == "?":
            res2 = 60
        elif d == "?":
            res2 = 6
        elif e == "?":
            res2 = 10
        else:
            res2 = 1

        return res1 * res2