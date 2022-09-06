def sqrt(n, p):
    l, r = 0, n
    root = 0.0
    while l <= r:
        mid = l + (r-l) // 2
        if mid * mid == n:
            return mid 
        elif mid * mid > n:
            r = mid - 1
        else:
            l = mid + 1
    
    incr = 0.1
    for i in range(p):
        while root * root <= n:
            root += incr
        root -= incr
        incr /= 10
    return root


if __name__ == "__main__":
    n = 36
    p = 3
    print("%.3f" % sqrt(n, p))
