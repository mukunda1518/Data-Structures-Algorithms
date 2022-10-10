if __name__ == "__main__":
    n, k = map(int, input().split())
    adj_matx = [
        [0] * n for i in range(n) ]
    for _ in range(k):
        r, c = map(int, input().split())
        adj_matx[r][c] = 1
        adj_matx[c][r] = 1

    for row in adj_matx:
        print(*row)