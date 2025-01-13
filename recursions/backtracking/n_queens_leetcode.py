# Leetcode : https://leetcode.com/problems/n-queens/description/

# Column based approach



class Solution:

    def is_safe_to_place_queen(self, row, col, n, board):
        # check upper diagonal
        t_row = row - 1
        t_col = col - 1

        while t_row >= 0 and t_col >= 0:
            if board[t_row][t_col] == 'Q':
                return False
            t_row -= 1
            t_col -= 1

        # check the row
        t_col = col - 1
        while t_col >= 0:
            if board[row][t_col] == 'Q':
                return False
            t_col -= 1

        # check for lower diagonal
        t_row = row + 1
        t_col = col - 1
        while t_row < n and t_col >= 0:
            if board[t_row][t_col] == 'Q':
                return False
            t_row += 1
            t_col -= 1

        return True


    def get_all_possible_ways(self, col, n, board, res):
        if col == n:
            res.append(["".join(row) for row in board])
            return

        for row in range(n):
            if self.is_safe_to_place_queen(row, col, n, board):
                board[row][col] = "Q"
                self.get_all_possible_ways(col+1, n, board, res)
                board[row][col] = "."

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [ ["."] * n for _ in range(n)]
        res = []
        self.get_all_possible_ways(0, n, board, res)
        return res



class Solution1:

    def get_all_possible_ways(self, col, n, board, res, left_row, lower_diagonal, upper_diagonal):
        if col == n:
            res.append(["".join(row) for row in board])
            return

        for row in range(n):
            if left_row[row] == 0 and lower_diagonal[row + col] == 0 and upper_diagonal[n - 1 + col - row] == 0:
                board[row][col] = "Q"
                left_row[row] = 1
                lower_diagonal[row + col] = 1
                upper_diagonal[n - 1 + col - row] = 1
                self.get_all_possible_ways(col+1, n, board, res, left_row, lower_diagonal, upper_diagonal)
                board[row][col] = "."
                left_row[row] = 0
                lower_diagonal[row + col] = 0
                upper_diagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [ ["."] * n for _ in range(n)]
        left_row = [0] * n
        upper_diagonal = [0] * (2 * n - 1)
        lower_diagonal = [0] * (2 * n - 1)
        res = []
        self.get_all_possible_ways(0, n, board, res, left_row, lower_diagonal, upper_diagonal)
        return res
