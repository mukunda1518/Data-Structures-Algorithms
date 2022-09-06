from collections import deque

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p, c = map(int, input().split())
        ids = list(range(1, p+1))
        dq = deque(ids)
        for _ in range(c):
            oper = input().split()
            if oper[0] == "N":
                print(dq[0], end=" ")
                dq.append(dq.popleft())
            elif oper[0] == "E":
                id_ = int(oper[1])
                dq.remove(id_)
                dq.appendleft(id_)
        print()
