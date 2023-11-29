

def find_sqrt_of_number():
    n = 40
    root = None
    s, e = 0, n
    # to find the sqrt root
    while s < e:
        root = s + (e - s) // 2
        if root * root == n:
            return root
        elif root * root < n:
            s = root + 1
        else:
            e = root - 1
    # print(root)
    # # to find the precession upto 2 values
    # incr = 0.1
    # for _ in range(2):
    #     while root * root <= n:
    #         root += incr
    #     root -= incr
    #     print(root)
        # incr /= 10

    return root


if __name__ == "__main__":
    print(find_sqrt_of_number())
