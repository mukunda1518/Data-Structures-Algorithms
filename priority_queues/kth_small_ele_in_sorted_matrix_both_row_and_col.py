# Leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from queue import PriorityQueue


def get_kth_smallest_element(matrix, n, k):
    pq = PriorityQueue()
    rows = min(n, k)
    # Picking up the first element of each row 
    for i in range(rows):
        pq.put((matrix[i][0], (i, 0)))
    
    while k:
        least_val, (i, j) = pq.get()
        if j < n - 1:
            pq.put((matrix[i][j+1], (i, j+1)))
        k -= 1 
    return least_val

    
if __name__ == "__main__":
    n, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(get_kth_smallest_element(matrix, n, k))