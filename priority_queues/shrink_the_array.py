from queue import PriorityQueue

def shrink_the_array(nums, n):
    pq = PriorityQueue()
    
    for num in nums:
        pq.put(-num)
    
    while pq.qsize() > 1:
        first = -1 * pq.get()
        second = -1 * pq.get()
        if first != second:
            diff = abs(first - second)
            pq.put(-diff)
    if pq.qsize() == 1:
        print(-1 * pq.get())
    else:
        print(-1)
    

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    shrink_the_array(nums, n)