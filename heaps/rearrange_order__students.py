from heapq import heapify, heappop, heappush

def sort_k(ids_order, n, k):
    heap = ids_order[:k+1]
    heapify(heap)
    
    target_index = 0
    for i in range(k+1, n):
        ids_order[target_index] = heappop(heap)
        heappush(heap, ids_order[i])
        target_index += 1 
    
    while heap:
        ids_order[target_index] = heappop(heap)
        target_index += 1 

if __name__ == "__main__":
    n, k = map(int, input().split())
    ids_order = list(map(int, input().split()))
    sort_k(ids_order, n, k)
    print(*ids_order)
    