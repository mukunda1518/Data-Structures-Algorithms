def check_odd_or_even(n):
    if n & 1 == 1:
        print("Odd")
    else:
        print("Even")


if __name__ == "__main__":
    n1 = 17
    n2 = 46
    check_odd_or_even(n1)
    check_odd_or_even(n2)