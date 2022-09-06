def power(x, n):
    if n == 0:
        return 1
    sub = power(x, n // 2)

    if n % 2 == 0:
        return sub * sub
    else:
        return x * sub * sub


if __name__ == "__main__":
    print(power(3, 4))
