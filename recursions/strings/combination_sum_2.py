def helper(up, p, target, res):
    sum_p = sum(p)
    if sum_p == target:
        res.append(p.copy())
    if sum_p >= target:
        return
    prev = -1
    for i in range(len(up)):
        if up[i] == prev:
            continue
        p.append(up[i])
        helper(up[i+1:], p, target, res)
        p.pop()
        prev = up[i]


if __name__ == "__main__":
    list = [10, 1, 2, 7, 6, 1, 5]
    list.sort()
    res = []
    helper(list, [], 8, res)
    print(res)