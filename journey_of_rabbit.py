def get_start_index(n, carrots, distances):
    for i in range(n):
        if carrots[i] < distances[i]:
            continue
        curr_carrots = carrots[i]
        end = i 
        j = i + 1 
        d = i 
        while j != end and curr_carrots >= distances[d]:
            if j == n:
                j = 0
            curr_carrots -= distances[d]
            curr_carrots += carrots[j]
            j += 1 
            d += 1 
            if d == n:
                d = 0
        if j == end:
            return end
    return -1

if __name__ == "__main__":
    n = int(input())
    carrots = []
    distances = []
    for _ in range(n):
        c, d = map(int, input().split())
        carrots.append(c)
        distances.append(d)
    print(get_start_index(n, carrots, distances))
    
    