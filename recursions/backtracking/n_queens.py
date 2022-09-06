def is_safe_to_place(board, r, c):
    # check vertical
    for i in range(r):
        if board[i][c] == "Q":
            return False
    # check diagonal left
    k = min(r, c)
    for i in range(1, k + 1):
        if board[r - i][c - i] == "Q":
            return False
    # check diagonal right
    k = min(r, len(board[0]) - c - 1)
    for i in range(1, k + 1):
        if board[r - i][c + i] == "Q":
            return False
    return True


def get_all_possibilities(board, r):
    if r == len(board):
        for row in board:
            print(row)
        print()
        return 1
    count = 0
    # placing the queen and checking for every row and column
    for c in range(len(board[0])):

        if is_safe_to_place(board, r, c):
            board[r][c] = "Q"
            count += get_all_possibilities(board, r+1)
            board[r][c] = "x"

    return count


if __name__ == "__main__":
    n = int(input())
    board = [["x"] * n for i in range(n)]
    print("No of Solutions = ", get_all_possibilities(board, 0))
