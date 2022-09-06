from queue import PriorityQueue

def get_kth_pencil(labels, n, k):
    pq = PriorityQueue()
    for label in labels:
        pq.put(label)
    
    count = 1 
    while count < k:
        interval = pq.get()
        if interval[0] < interval[1]:
            pq.put([interval[0] + 1, interval[1]])
        count += 1 
    return pq.queue[0][0]

if __name__ == "__main__":
    n, k = map(int, input().split())
    labels = []
    for _ in range(n):
        label = list(map(int, input().split()))
        labels.append(label)
    print(get_kth_pencil(labels, n, k))
    