# 2943. Maximize Area of Square Hole in Grid

# You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

# You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

# Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()

        horizontal = curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                curr += 1
            else:
                horizontal = max(curr, horizontal)
                curr = 1
        horizontal = max(horizontal, curr)
        
        vertical = curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                curr += 1
            else:
                vertical = max(curr, vertical)
                curr = 1
        vertical = max(vertical, curr)

        res = min(horizontal + 1, vertical + 1)
        return res * res