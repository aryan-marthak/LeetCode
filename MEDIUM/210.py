# 210. Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c: [] for c in range(numCourses)}
        for i, j in prerequisites:
            prereq[i].append(j)
        
        output = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for i in prereq[course]:
                if dfs(i) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output