def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
    print(n)


if __name__ == "__main__":
    n = int(input())
    fun(n)