from queue import PriorityQueue

def get_max_pillar_index(heights, n, bricks, ladders):
    pq = PriorityQueue()
    for i in range(1, n):
        climb = heights[i] - heights[i-1]
        if climb <= 0:
            continue
        pq.put(climb)
        if pq.qsize() <= ladders:
            continue
        bricks -= pq.get()
        
        if bricks < 0:
            return i -1 
    return n - 1
        
if __name__ == "__main__":
    n, b, l = map(int, input().split())
    heights = list(map(int, input().split()))
    print(get_max_pillar_index(heights, n, b, l))