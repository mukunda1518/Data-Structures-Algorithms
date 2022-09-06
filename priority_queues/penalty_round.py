from queue import PriorityQueue

def get_final_scores(nums, k):
    pq = PriorityQueue()
    for num in nums:
        pq.put(-num)
    for i in range(k):
        num = -1 * pq.get()
        num = num // 2
        pq.put(-num)
    sum_ = 0
    while pq.qsize():
        sum_ += -1 * pq.get()
    return sum_
        

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(get_final_scores(nums, k))