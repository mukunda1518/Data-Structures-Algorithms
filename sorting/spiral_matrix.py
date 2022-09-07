# Leetcode: https://leetcode.com/problems/spiral-matrix/

if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    r, c = 0, 0
    while r < m and c < n:

        # Right elements
        for i in range(c, n):
            print(matrix[r][i], end=" ")

        # Down Elements
        r += 1
        for i in range(r, m):
            print(matrix[i][n - 1], end=" ")
        n -= 1

        # Left Elements
        if r < m:
            for i in range(n - 1, c - 1, -1):
                print(matrix[m - 1][i], end=" ")
            m -= 1
            # Upside Elements
        if c < n:
            for i in range(m - 1, r - 1, -1):
                print(matrix[i][c], end=" ")
            c += 1


