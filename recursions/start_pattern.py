def print_pattern(n):
    if n == 0:
        return
    print("*" * n)
    print_pattern(n-1)


def triangle(r, c):
    if r == 0:
        return
    if c < r:
        print("*", sep=" ")
        triangle(r, c + 1)
    else:
        print("\n")
        triangle(r - 1, 0)


print_pattern(4)
triangle(5, 0)
