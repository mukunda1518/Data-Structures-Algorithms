# Remainder Jarvis - Check in problem images folder

import heapq


def get_task_order(tasks, k):
    tasks_order = []
    heapq.heapify(tasks)
    while k:
        duration, id_, incr = heapq.heappop(tasks)
        tasks_order.append(id_)
        duration += incr
        heapq.heappush(tasks, [duration, id_, incr])
        k -= 1
    return tasks_order


if __name__ == "__main__":
    n, k = map(int, input().split())
    tasks = []
    for _ in range(n):
        id_, duration = map(int, input().split())
        tasks.append([duration, id_, duration])
    print(*get_task_order(tasks, k))

