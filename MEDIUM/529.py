# 529. Minesweeper

# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

#     'M' represents an unrevealed mine,
#     'E' represents an unrevealed empty square,
#     'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
#     digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
#     'X' represents a revealed mine.

# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

#     If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
#     If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
#     If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
#     Return the board when no more squares will be revealed.

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dirs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, 1), (0, -1),
            (1, -1), (1, 0), (1, 1)
        ]

        def dfs(a, b):
            mines = 0
            for i, j in dirs:
                nr, nc = i + a, j + b
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == "M":
                        mines += 1

            if mines > 0:
                board[a][b] = str(mines)
                return
            
            board[a][b] = "B"

            for i, j in dirs:
                nr, nc = i + a, j + b
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "E":
                    dfs(nr, nc)

        a, b = click
        if board[a][b] == "M":
            board[a][b] = "X"
        else:
            dfs(a, b)
        return board