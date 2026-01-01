# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        for i, j in intervals[1:]:
            last = res[-1][1]
            if i <= last:
                res[-1][1] = max(last, j)
            else:
                res.append([i, j])
        return res