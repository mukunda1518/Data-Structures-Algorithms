from collections import deque
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    queue = deque()
    i, j = 0, 0
    while j < len(nums):
        if nums[j] < 0:
            queue.append(nums[j])
        if j - i + 1 == k:
            if not queue:
                print(0, end = " ")
            else:
                if queue[0] == nums[i]:
                    print(queue.popleft(), end=" ")
                else:
                    print(queue[0], end=" ")
            i += 1 
        j += 1
    
