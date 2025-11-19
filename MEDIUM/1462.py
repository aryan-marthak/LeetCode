# 1462. Course Schedule IV

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

#     For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for i, j in queries:
            res.append(i in prereqMap[j])
        return res
    
    #  BRUTE FORCE TLE
    
        # adj = [[] for i in range(numCourses)]
        # for i, j in prerequisites:
        #     adj[i].append(j)

        # def dfs(node, target):
        #     if node == target:
        #         return True
        #     for nei in adj[node]:
        #         if dfs(nei, target):
        #             return True
        #     return False

        # res = []
        # for i, j in queries:
        #     res.append(dfs(i, j))
        # return res