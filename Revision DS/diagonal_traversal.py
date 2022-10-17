# def get_diagonal_elements(matrix):
#     arr = []
#     m = len(matrix)
#     n = len(matrix[0])
#     i = 0
#     while i < m:
#         k, j = i, 0
#         while k >= 0 and j < n:
#             if matrix[k][j] != "0":
#                 arr.append(matrix[k][j])
#             k -= 1
#             j += 1
#         i += 1

#     j = 1
#     while j < n:
#         k, i = j, m - 1
#         while k < n:
#             if matrix[i][k] != "0":
#                 arr.append(matrix[i][k])
#             i -= 1
#             k += 1
#         j += 1

#     return arr

# if __name__ == "__main__":
#     m = int(input())
#     cols_len = []
#     matrix = []
#     for _ in range(m):
#         row = list(map(int, input().split()))
#         r_len = row[0]
#         cols_len.append(r_len)
#         matrix.append((row[1:], r_len))
#     maxi = max(cols_len)
#     new_matrix = []
#     for row, r_len in matrix:
#         rem = ["0"] * (maxi - r_len)
#         new_row = row + rem
#         new_matrix.append(new_row)
#     diagonal_elements = get_diagonal_elements(new_matrix)
#     print(*diagonal_elements)

def find_diagonal_order(nums, rows, cols):
    n = rows + cols - 1
    res = [[] for _ in range(n)]
    dia = []
    for i, r in enumerate(nums):
        for j, a in enumerate(r):
            res[i + j].append(a)
    for i in range(len(res)):
        for num in reversed(res[i]):
            dia.append(num)
    return dia


if __name__ == "__main__":
    nums = []
    res = []
    cols = []
    rows = int(input())
    for i in range(rows):
        v = [int(val) for val in input().split()]
        cols.append(v[0])
        nums.append(v[1:])
    max_cols = max(cols)
    res = find_diagonal_order(nums, rows, max_cols)
    print(*res)






