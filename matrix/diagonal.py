if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    sum = m + n - 1
    for s in range(sum):
        if s % 2 == 0:
            if s < m:
               r = s
               c = s - r
            else:
                r = m - 1
                c = s - r
            while r < m and c < n and r >= 0  and c >= 0:
                print(matrix[r][c], end = " ")
                r -= 1
                c += 1
        else:
            if s < n:
                c = s
                r = s - c
            else:
               c = n - 1
               r = s - c
            while r < m and c < n and r >= 0 and c >= 0:
                print(matrix[r][c], end = " ")
                r += 1
                c -= 1
