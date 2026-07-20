# 1443. Minimum Time to Collect All Apples in a Tree

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i:[] for i in range(n) }

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(cur, par):
            time = 0
            for child in adj[cur]:
                if child == par:
                    continue
                ctime = dfs(child, cur)
                if ctime or hasApple[child]:
                    time += ctime + 2
            return time
        return dfs(0, -1)