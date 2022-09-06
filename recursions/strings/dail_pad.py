
def dail_pad(p, up):
    if up == "":
        print(p)
        return
    digit = int(up[0])
    s = (digit - 1) * 3
    e = (digit) * 3
    for i in range(s, e):
        char = chr(i + 97)
        dail_pad(p + char, up[1:])

def dail_pad_list(p, up):
    if up == "":
        return[p]
    digit = int(up[0])
    s = (digit - 1) * 3
    e = (digit) * 3
    arr = []
    for i in range(s, e):
        char = chr(i + 97)
        arr.extend(dail_pad_list(p + char, up[1:]))
    return arr
    
if __name__ == "__main__":
    dail_pad("", "12")
    print(dail_pad_list("", "12"))
