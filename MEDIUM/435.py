# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# GREEDY
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][1]
        for i, j in intervals[1:]:
            if i >= end:
                end = j
            else:
                res += 1
                end = min(end, j)
        return res