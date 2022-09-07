# Leetcode : https://leetcode.com/problems/kth-largest-element-in-an-array/

from queue import PriorityQueue

def get_kth_largest(nums, k):
    pq = PriorityQueue()
    for num in nums:
        if pq.qsize() < k:
            pq.put(num)
        else:
            if pq.queue[0] < num:
                pq.get()
                pq.put(num)
    return pq.get()

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(get_kth_largest(nums, k))