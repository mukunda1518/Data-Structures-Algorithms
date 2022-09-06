def get_all_possible_knight_positions(board, r, c, knights):
    if knights == 0:
        for row in board:
            print("".join(row))
        print()
        return 1

    count = 0
    if r == len(board) - 1 and c == len(board):
        return 0
    
    if c == len(board):
        count += get_all_possible_knight_positions(board, r + 1, 0, knights)
        return count
    
    if is_safe_to_place(board, r, c):
        board[r][c] = "K"
        count += get_all_possible_knight_positions(board, r, c+1, knights - 1)
        board[r][c] = "x"

    count += get_all_possible_knight_positions(board, r, c+1, knights)
    return count


def is_safe_to_place(board, r, c):
    if is_valid(board, r - 2, c - 1):
        if board[r - 2][c - 1] == "K":
            return False

    if is_valid(board, r - 2, c + 1):
        if board[r - 2][c + 1] == "K":
            return False

    if is_valid(board, r - 1, c - 2):
        if board[r - 1][c - 2] == "K":
            return False

    if is_valid(board, r - 1, c + 2):
        if board[r - 1][c + 2] == "K":
            return False
    return True


def is_valid(board, r, c):

    if r >= 0 and r < len(board) and c >= 0 and c < len(board):
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    board = [["x"] * n for i in range(n)]
    # get_all_possible_knight_positions(board, 0, 0, n)
    print("Total Possible ways : ", get_all_possible_knight_positions(board, 0, 0, n))
