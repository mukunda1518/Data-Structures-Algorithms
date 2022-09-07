# Leetcode: https://leetcode.com/problems/k-th-smallest-prime-fraction/

from queue import PriorityQueue


def find_kth_smallest_fraction(nums, n, k):
    pq = PriorityQueue()
    for i in range(n-1):
        if i < k:
            pq.put((nums[i]/nums[-1], (i, n-1)))
    i, j = -1, -1
    while k:
        val, (i, j) = pq.get()
        if j > i:
            pq.put((nums[i]/nums[j-1], (i, j-1)))
        k -= 1 
    print(nums[i], nums[j])
    
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    find_kth_smallest_fraction(nums, n, k)