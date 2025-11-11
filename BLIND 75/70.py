# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        # FIBONACCI SEQUENCE
        one, two = 1, 1 

        for i in range(n-1):
            temp = two
            two = one + two
            one = temp
        return two

        # DP ARRAY
        ways = [1, 1, 2]
        for step in range(3, n + 1):
            ways.append(ways[step - 1] + ways[step - 2])
        return ways[n]