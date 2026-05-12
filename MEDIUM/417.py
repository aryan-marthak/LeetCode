# 417. Pacific Atlantic Water Flow

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        res = []
        pac = [[False for i in range(n)] for j in range(m)]
        atl = [[False for i in range(n)] for j in range(m)]

        def helper(row, col, heights, ocean):
            ocean[row][col] = True
            Ds = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for i, j in Ds:
                if i >= 0 and j >= 0 and i < m and j < n and not ocean[i][j] and heights[i][j] >= heights[row][col]:
                    helper(i, j, heights, ocean)
            return

        for i in range(m):
            helper(i, 0, heights, pac)
            helper(i, n - 1, heights, atl)
        
        for i in range(n):
            helper(0, i, heights, pac)
            helper(m - 1, i, heights, atl)
        
        for i in range(m):
            for j in range(n):
                if atl[i][j] and pac[i][j]:
                    res.append([i, j])
        return res
