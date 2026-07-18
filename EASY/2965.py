# 2965. Find Missing and Repeated Values

# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        Map = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in Map:
                    Map[grid[i][j]] = 0
                Map[grid[i][j]] += 1

        a, b = 0, 0
        for i in range(1, len(grid) ** 2 + 1):
            if i not in Map:
                b = i
            elif Map[i] == 2:
                a = i
        return [a, b]