from collections import deque
def get_decoded_str(word):
    dq = deque([])
    n = len(word)
    i = 0
    while i < n:
        if word[i] in "><":
            k = i 
            sub_str = ""
            i += 1
            while i < n and (word[i] not in "><"):
                sub_str += word[i]
                i += 1 
            if sub_str and word[k] == ">":
                dq.append(sub_str)
            elif sub_str and word[k] == "<":
                dq.appendleft(sub_str)
        else:
            dq.append(word[i])
            i += 1 
    return "".join(dq) if dq else -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word = input()
        print(get_decoded_str(word))