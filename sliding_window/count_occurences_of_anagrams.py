from collections import Counter
def search(pat, txt):
    res = 0
    k = len(pat)
    map = dict(Counter(pat))
    count = len(map)
    i = 0
    for j in range(len(txt)):
        if txt[j] in map:
            map[txt[j]] -= 1 
            if map[txt[j]] == 0:
                count -= 1 
        if j - i + 1 == k:
            if count == 0:
                res += 1
            if txt[i] in map:
                if map[txt[i]] == 0:
                    count += 1
                map[txt[i]] += 1
            i += 1 
        j += 1
    return res

if __name__ == "__main__":
    txt = input()
    pat = input()
    print(search(pat, txt))