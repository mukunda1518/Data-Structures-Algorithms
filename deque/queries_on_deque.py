from collections import deque
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    q = int(input())
    dq = deque(nums)
    for _ in range(q):
        oper = list(map(int, input().split()))
        if oper[0] == 0:
            dq.append(dq.popleft())
        elif oper[0] == 1:
            dq.appendleft(dq.pop())
        elif oper[0] == 2:
            index, num = oper[1], oper[2]
            dq[index] = num
        elif oper[0] == 3:
            index = oper[1]
            print(dq[index], end=" ")
    
            
        