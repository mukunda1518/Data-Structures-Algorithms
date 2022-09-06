from collections import deque

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    queue = deque([])
    arr = []
    i = 0
    for j in range(len(nums)):
        while queue and nums[j] > queue[-1]:
            queue.pop()
        queue.append(nums[j])
        if j - i + 1 == k:
            arr.append(queue[0])
            if queue[0] == nums[i]:
                queue.pop()
            i += 1
        j += 1
    
    print(*arr)
