from queue import PriorityQueue
from collections import Counter

def get_count(s, k):
    pq = PriorityQueue()
    s_dict = dict(Counter(s))
    values = list(s_dict.values())
    for val in values:
        pq.put(-val)
    for _ in range(k):
        num = -1 * pq.get()
        num -= 1 
        pq.put(-1 * num)
    sum_ = 0
    for num in pq.queue:
        sum_ += num * num
    return sum_
if __name__ == "__main__":
    s = input()
    k = int(input())
    print(get_count(s, k))