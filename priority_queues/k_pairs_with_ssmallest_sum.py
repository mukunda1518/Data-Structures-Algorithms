# Leetcode: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from queue import PriorityQueue


def get_pairs(m_nums, n_nums, m, n, k):
    pq = PriorityQueue()
    for i in range(m):
        if i < k:
            pq.put((m_nums[i] + n_nums[0], (i, 0)))
    res = []
    while k and pq.qsize() > 0:
        sum_, (i, j) = pq.get()
        res.append((m_nums[i], n_nums[j]))

        if j + 1 < n:
            pq.put((m_nums[i] + n_nums[j + 1], (i, j + 1)))
        k -= 1
    return res


if __name__ == "__main__":
    m = int(input())
    m_nums = list(map(int, input().split()))
    n = int(input())
    n_nums = list(map(int, input().split()))
    k = int(input())
    res = get_pairs(m_nums, n_nums, m, n, k)
    for each in res:
        print(*each)