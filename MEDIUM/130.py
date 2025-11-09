# 130. Surrounded Regions

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

#     Connect: A cell is connected to adjacent cells horizontally or vertically.
#     Region: To form a region connect every 'O' cell.
#     Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if (board[i][j] == "O" and (i in [0, m - 1]) or j in [0, n - 1]):
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"