# Leetcode : https://leetcode.com/problems/brick-wall/

from collections import defaultdict

def least_bricks(bricks_widths):
    edges_map = defaultdict(int)
    for row in bricks_widths:
        width = 0
        for j in range(0, len(row) - 1):
            width += row[j]
            edges_map[width] += 1 
    
    row_common_edges = max(edges_map.values()) if edges_map else 0
    return len(bricks_widths) - row_common_edges

if __name__ == "__main__":
    bricks_widths = []
    n = int(input())
    for _ in range(n):
        row = list(map(int, input().split()))
        row.pop()
        bricks_widths.append(row)
    count = least_bricks(bricks_widths)
    print(count)
    