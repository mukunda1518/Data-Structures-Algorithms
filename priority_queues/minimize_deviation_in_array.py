# https://leetcode.com/problems/minimize-deviation-in-array/


from queue import PriorityQueue
def get_min_diff(nums, n):
    pq = PriorityQueue()
    min_val = float("inf")
    for num in nums:
        if num % 2 == 1:
            num *= 2 
        if num < min_val:
            min_val = num
        pq.put(-num)  

    min_diff = float("inf")

    while True:
        max_val = -1 * pq.get()
        min_diff = min(min_diff, max_val - min_val)
        if max_val % 2 == 1:
            break
        max_val = max_val // 2
        min_val = min(min_val, max_val)
        pq.put(-1 * max_val)
    return min_diff

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(get_min_diff(nums, n))