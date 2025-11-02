# 1267. Count Servers that Communicate

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        count_r = [0] * m
        count_c = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_r[i] += 1
                    count_c[j] += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (count_r[i] > 1 or count_c[j] > 1):
                    res += 1
        return res