from queue import PriorityQueue
def distribution_possible():
    n, m, k = map(int, input().split())
    old = list(map(int, input().split()))
    extra = list(map(int, input().split()))
    old_pq = PriorityQueue()
    e_pq = PriorityQueue()
    for num in old:
        old_pq.put(num)
    for num in extra:
        e_pq.put(-1 * num)
    
    while not e_pq.empty():
        num = -1 * e_pq.get()
        num2 = old_pq.get()
        if num + num2 <= k:
            old_pq.put(num + num2)
        else:
            return "NO"
    return "YES"
            
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(distribution_possible())