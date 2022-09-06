from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    k = max(queries)
    dq = deque(nums)
    res = [(nums[0], nums[1])]
    for i in range(1, k+1):
        a = dq.popleft()
        b = dq.popleft()
        if a > b:
            dq.appendleft(a)
            dq.append(b)
        if a <= b:
            dq.appendleft(b)
            dq.append(a)
        res.append((dq[0], dq[1]))
    for i in queries:
        print(*res[i])
        
    
    
    