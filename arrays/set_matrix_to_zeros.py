# Leetcode : https://learning.ccbp.in/crash-course/coding/5f7cf3e8-4556-4fda-a85d-c2ea2323f4ec

def set_to_zeros(matrix):
    # is first row contains zeros
    is_first_row_zero = False
    for c in range(n):
        if matrix[0][c] == 0:
            is_first_row_zero = True

    # is first column contains zeros
    is_first_col_zero = False
    for r in range(m):
        if matrix[r][0] == 0:
            is_first_col_zero = True

    # Find Zeros stor that info in first row and column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

                # Set Zeros expect the first and last row
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set zeros for first row and column if needed

    if is_first_row_zero:
        for c in range(n):
            matrix[0][c] = 0

    if is_first_col_zero:
        for r in range(m):
            matrix[r][0] = 0

    # print updated matrix
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    set_to_zeros(matrix)
