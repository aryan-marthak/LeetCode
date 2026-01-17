# 3047. Find the Largest Area of Square Inside Two Rectangles

# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        s = 0
        l = len(bottomLeft)

        for i in range(l):
            for j in range(i + 1, l):
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                max_x = min(topRight[i][0], topRight[j][0])
                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
                max_y = min(topRight[i][1], topRight[j][1])

                if min_x < max_x and min_y < max_y:
                    res = min(max_x - min_x, max_y - min_y)
                    s = max(s, res)
        return s * s