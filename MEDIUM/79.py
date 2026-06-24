# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        text_len = len(word)
        if m == 1 and n == 1:
            return board[0][0] == word
        
        def backtrack(i, j, index):
            if index == text_len:
                return True

            if board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                a, b = i + x, j + y
                if a < m and b < n and a >= 0 and b >= 0:
                    if backtrack(a, b, index + 1):
                        return True

            board[i][j] = temp
            return False 

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
    
# Time complexity: O(m * n * 4^L), where L is the length of the word. In the worst case, we might explore all 4 directions for each letter in the word.
# Space complexity: O(L), where L is the length of the word. This is the