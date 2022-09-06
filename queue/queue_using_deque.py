from collections import deque

def enqueue(queue, x):
    queue.append(x)

def dequeue(queue):
    if not queue:
        return -1
    return queue.popleft()

# main
n = int(input())
queue = deque()

A = []
for _ in range(n):
    arr = [x for x in input().split()]
    A.append(arr)


for i in range(n):
    if A[i][0] == "A":
        enqueue(queue, A[i][1])
    elif A[i][0] == "B":
        print(dequeue(queue), end=" ")