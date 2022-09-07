# Leetcode: https://leetcode.com/problems/best-meeting-point/

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    row = []
    col = []
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1:
                row.append(r)
                col.append(c)
    col.sort()
    len_ = len(row)
    mid_row = row[len_ // 2] if len_ % 2 else (row[len_ // 2] + row[len_ // 2 - 1]) // 2
    mid_col = col[len_ // 2] if len_ % 2 else (col[len_ // 2] + col[len_ // 2 - 1]) // 2

    min_dist = 0
    for i in range(len_):
        min_dist += abs(mid_row - row[i]) + abs(mid_col - col[i])
    print(min_dist)


