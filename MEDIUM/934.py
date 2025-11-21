# 934. Shortest Bridge

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N
        
        visit = set()
        def dfs(r , c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visit):
                return
            visit.add((r, c))
            for i, j in direction:
                dfs(r + i, c + j)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for x in range(len(q)):
                    r, c = q.popleft()
                    for i, j in direction:
                        curI, curJ = r + i, c + j   
                        if invalid(curI, curJ) or (curI, curJ) in visit:
                            continue
                        if grid[curI][curJ]:
                            return res
                        q.append((curI, curJ))
                        visit.add((curI, curJ))
                res += 1
                
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()