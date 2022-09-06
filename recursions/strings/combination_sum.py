def helper(u_p, p, target, res):
    sum_of_p = sum(p)
    if sum_of_p == target:
        res.append(p.copy())
        return
    elif sum_of_p > target or not u_p:
        return
    p.append(u_p[0])
    helper(u_p, p, target, res)
    p.pop()
    helper(u_p[1:], p, target, res)
    return res


if __name__ == "__main__":
    print(helper([2, 3, 6, 7], [], 7, []))