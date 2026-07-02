# 973. K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        mindist = []
        heapq.heapify(mindist)
        for i, v in enumerate(points):
            dist = sqrt(v[0]**2 + v[1]**2)
            heapq.heappush(mindist, [dist, i])
        while k > 0:
            i, j = heapq.heappop(mindist)
            res.append(points[j])
            k -= 1
        return res

# Brute Force
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        while k > 0:
            temp = float('inf')
            x = -1
            for i, v in enumerate(points):
                dist = sqrt(v[0]**2 + v[1]**2)
                if dist < temp:
                    temp = dist
                    x = i
            res.append(points.pop(x))
            k -= 1
        return res              