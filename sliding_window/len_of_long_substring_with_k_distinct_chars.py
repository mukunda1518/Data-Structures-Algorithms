if __name__ == "__main__":
    s = input()
    k = int(input())
    map = {}
    i = 0
    max_len = 0
    for j in range(len(s)):
        if s[j] not in map:
            map[s[j]] = 1
        else:
            map[s[j]] += 1
        if len(map) == k:
            max_len = max(max_len, j - i + 1)
        while len(map) > k:
            map[s[i]] -= 1
            if map[s[i]] == 0:
                del map[s[i]]
            i += 1
    print(max_len)
    # print(max(max_len, j - i + 1))
        