# 3453. Separate Squares I

# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted multiple times.

# BINARY SEARCH + AREA CALCULATION
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def helper(mid, squares):
            area = 0.0
            for x, y, l in squares:
                if mid >= y + l:
                    area += l * l
                elif y < mid < y + l:
                    area += l * (mid - y)
            return area
    
        total = 0.0
        miny = float('inf')
        maxy = float('-inf')

        for x, y, l in squares:
            total += l * l
            miny = min(miny, y)
            maxy = max(maxy, y + l)
        
        l, r = miny, maxy
        target = total / 2.0

        while l < r:
            if r - l < 10 ** -5:
                break
            mid = (r + l) / 2
            if helper(mid, squares) < target:
                l = mid
            else:
                r = mid
        return r