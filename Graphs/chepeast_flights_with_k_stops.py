# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=22




# Time Complexity = O(V * E)

from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        min_cost = [float("inf")] * n
        dq = deque([(0, src, 0)]) # (stops, node, cost)

        while dq:
            stops, city, cost = dq.popleft()

            if stops > k:
                continue
            
            for next_city, price in graph[city]:
                if cost + price < min_cost[next_city]:
                    min_cost[next_city] = cost + price
                    dq.append((stops + 1, next_city, cost + price))

        return -1 if min_cost[dst] == float("inf") else min_cost[dst]

        