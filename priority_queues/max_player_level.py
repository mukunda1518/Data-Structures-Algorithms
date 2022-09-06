from queue import PriorityQueue

def get_no_of_levels_a_player_can_reach(damages, n, x, y):
    y_pq = PriorityQueue()
    levels = 1 
    for i in range(1, n):
        diff = damages[i] - damages[i-1]
        if diff <= 0:
            levels += 1
            continue
        
        y_pq.put(diff)
        if y_pq.qsize() > y:
            x -= y_pq.get()
        if x < 0:
            break
        levels += 1

    return levels

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    damages = list(map(int, input().split()))
    print(get_no_of_levels_a_player_can_reach(damages, n, x, y))