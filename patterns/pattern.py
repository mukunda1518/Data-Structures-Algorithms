def pattern1(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def pattern4(n):
    for row in range(0, 2 * n - 1):
        col = 2 * n - row -  1 if row >= n else row + 1
        for c in range(col):
            print("*", end = " ")
        print()

def pattern28(n):
    for row in range(0, 2 * n - 1):
        col = 2 * n - row -  1 if row >= n else row + 1
        spaces = n - col
        for s in range(spaces):
            print(" ", end="")
        for c in range(col):
            print("*", end = " ")
        print()

def pattern30(n):
    for row in range(1, n+1):
        space = n - row
        for s in range(n-row):
            print("  ", end="")
        for col in range(row, 0, -1):
            print(col, end=" ")
        for col in range(2, row + 1):
            print(col, end=" ")
        print()

def pattern17(n):
    for row in range(1, 2 * n):
        col = 2 * n - row if row > n else row
        spaces = n - col
        for s in range(spaces):
            print(" ", end="")
        for c in range(col, 0, -1):
            print(c, end="")
        for c in range(2, col + 1):
            print(c, end="")
        print()

def pattern31(num):
    n = num - 1
    for row in range(2 * n + 1):
        for col in range( 2 * n + 1):
            val = num - min(col, row, 2 * n - row, 2 * n - col)
            print(val, end = " ")
        print()



if __name__ == "__main__":
    pattern1(5)
    print()
    pattern2(5)
    print()
    pattern3(5)
    print()
    pattern4(5)
    print()
    pattern28(5)
    print()
    pattern30(5)
    print()
    pattern17(5)
    print()
    pattern31(4)