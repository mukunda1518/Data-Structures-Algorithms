import heapq

def get_total_score(nums, n, p, q):
    nums.sort()
    return sum(nums[p:q-1])

def get_total_score_using_heap(min_heap, n, p, q):
    heapq.heapify(min_heap)
    i = 1
    while i <= p:
        heapq.heappop(min_heap)
        i += 1 
    total = 0
    i = p + 1
    while i < q:
        total += heapq.heappop(min_heap)
        i += 1 
    return total

if __name__ == "__main__":
    n, p, q = map(int, input().split())
    nums = list(map(int, input().split()))
    # print(get_total_score(nums, n, p, q))
    print(get_total_score_using_heap(nums, n, p, q))
    