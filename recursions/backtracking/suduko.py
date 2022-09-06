import math


def is_safe_to_place(board, r, c, num):
    # check for column
    for i in range(len(board[0])):
        if board[r][i] == num:
            return False
    # check for row
    for i in range(len(board)):
        if board[i][c] == num:
            return False
    # check for sub_board
    sqrt_num = int(math.sqrt(len(board)))
    k = r - r % sqrt_num
    e = c - c % sqrt_num

    for i in range(k, k + sqrt_num):
        for j in range(e, e + sqrt_num):
            if board[i][j] == num:
                return False
    return True


def solve_sudoko_1(board, r, c):
    if r == len(board):
        return True

    if c == len(board[0]):
        solve_sudoko_1(board, r + 1, 0)
        return False

    if board[r][c] != ".":
        solve_sudoko_1(board, r, c+1)
        return False

    for i in range(1, len(board[0]) + 1):
        if is_safe_to_place(board, r, c, str(i)):
            board[r][c] = str(i)
            if (solve_sudoko_1(board, r, c+1)):
                return True
            else:
                board[r][c] = "."
    return False


def solve_sudoko(board):

    flag = True
    row = - 1
    col = -1
    # To replace r, c in arguments
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                row = i
                col = j
                flag = False
                break
        if not flag:
            break
    if flag:
        for row in board:
            print(row)
        return True
        # sudoko is solved

    for i in range(1, len(board[0])+1):
        if is_safe_to_place(board, row, col, str(i)):
            board[row][col] = str(i)
            if solve_sudoko(board):
                return True
            board[row][col] = "."
    return False






if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solve_sudoko(board))
