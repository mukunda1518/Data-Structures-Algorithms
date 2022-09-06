from queue import PriorityQueue

def maximize_profit(seats, m):
    pq = PriorityQueue()
    for seat in seats:
        pq.put(-1 * seat)
    
    profit = 0
    while m and not pq.empty():
        cost = -1 * pq.get()
        profit += cost
        cost -= 1 
        if cost > 0:
            pq.put(-1 * cost)
        m -= 1
    return profit

if __name__ == "__main__":
    n, m = map(int, input().split())
    seats = list(map(int, input().split()))
    print(maximize_profit(seats, m))
    