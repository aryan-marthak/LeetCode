# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    # Fibonacci Sequence

    def climbStairs(self, n):
        one, two = 1, 1 

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        
    # RECURRSION

        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)