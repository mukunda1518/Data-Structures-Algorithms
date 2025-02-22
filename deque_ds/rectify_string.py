from collections import deque
def get_updated_str(str_):
    dq = deque()
    for char in str_:
        if char != "<":
            dq.append(char)
        elif dq:
            dq.pop()
    return "".join(dq) if dq else -1

if __name__ == "__main__":
    t = int(input())
    strs = []
    for _ in range(t):
        strs.append(input())
    for str_ in strs:
        print(get_updated_str(str_))