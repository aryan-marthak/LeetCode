# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        lwall = rwall = 0
        max_l = [0] * len(height)        
        max_r = [0] * len(height)        
        for i in range(len(height)):
            j = -i -1
            max_l[i] = lwall
            max_r[j] = rwall
            lwall = max(lwall, height[i])
            rwall = max(rwall, height[j])
        Sum = 0
        for i in range(len(height)):
            pot = min(max_l[i], max_r[i])
            Sum += max(0, pot - height[i])
        return Sum