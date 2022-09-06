from queue import PriorityQueue
mod = 10 ** 9 + 7
def get_peformance_of_a_team(speeds, efficiencies, n, k):
    sp_eff = []
    for i in range(n):
        sp_eff.append((speeds[i], efficiencies[i]))
    sp_eff.sort(reverse=True, key=lambda val: val[1])
    pq = PriorityQueue()
    speed_sum = 0
    min_eff = float('+inf')
    max_perf = 0

    for i in range(n):
        if pq.qsize() == k:
            s, e = pq.get()
            speed_sum -= s
        pq.put(sp_eff[i])
        speed_sum += sp_eff[i][0]
        min_eff = min(min_eff, sp_eff[i][1])
        max_perf = max(max_perf, speed_sum * min_eff)
    return max_perf % mod
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    speeds = list(map(int, input().split()))
    efficiencies = list(map(int, input().split()))
    print(get_peformance_of_a_team(speeds, efficiencies, n, k))
    
    