def longestSubstring(s):
    l = 0
    max_len = 0
    set_a = set()
    for r in range(0, len(s)):
        while s[r] in set_a:
            set_a.remove(s[l])
            l += 1
        set_a.add(s[r])
        max_len = max(r - l + 1, max_len)
    return max_len


if __name__ == "__main__":
    s = input()
    map = {}
    max_len = 0
    i = 0
    for j in range(len(s)):
        if s[j] not in map:
            map[s[j]] = 1 
        else:
            map[s[j]] += 1 

        if len(map) == j - i + 1:
            max_len = max(max_len, j-i+1)
        while len(map) < j - i + 1:
            map[s[i]] -= 1 
            if map[s[i]] == 0:
                del map[s[i]]
            i += 1 
    print(max_len)