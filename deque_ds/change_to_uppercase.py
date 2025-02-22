from collections import deque
def get_updated_word(word):
    f = 0
    dq = deque()
    for char in word:
        if char != "@":
            dq.append(char)
            f = 0
        elif dq and len(dq) > f:
            dq[-1 - f] = dq[-1 - f].upper()
            f += 1 
    return "".join(dq)

def get_updated_word1(word):
    dq = deque()
    i = 0
    n = len(word)
    while i < n:
        if word[i] != "@":
            dq.append(word[i])
            i += 1
        else:
            # count the no of '@'
            freq = 0
            while i < n and word[i] == "@":
                freq += 1 
                i += 1 
            # store and update queue chars to upper case 
            temp = ""
            while len(dq) > 0 and freq > 0:
                temp += dq.pop().upper()
                freq -= 1 
            for char in temp[::-1]:
                dq.append(char)
    return "".join(dq)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word = input()
        print(get_updated_word(word))
        print(get_updated_word1(word))