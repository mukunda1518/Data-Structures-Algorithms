


# find 6th magic number
# 1st MN - 0001 = 1 * 5^1 = 5
# 2nd MN - 0010 = 1 * 5^2 = 25
# 3rd MN - 0011 = 1 * 5^2 + 1 * 5^1 = 30
# 4th MN - 0100 = 1 * 5^3 = 125
# 5th MN - 0101 = 1 * 5^3 + 1 * 5^1 = 130
# 6th MN - 0110 = 1 * 5^3 + 1 * 5^2 = 150


# Time Complexity : 

def find_magic_num(n):
    ans = 0
    base = 5
    while n:
        last = n & 1
        n = n >> 1
        ans += last * base
        base = base * 5
    print(ans)


if __name__ == "__main__":
    n = 6
    find_magic_num(n)
    