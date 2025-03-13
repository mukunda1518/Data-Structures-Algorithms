
# Leetcode - https://leetcode.com/problems/task-scheduler/description/

# Solution - https://leetcode.com/problems/task-scheduler/solutions/5806671/python3-detailed-intuition-explanation-with-max-heap-queue-counter/


# Time complexity:
# Main while loop:
# The number of iterations the loop runs is equal to the total time required to finish all tasks (including idle times). Hence, O(timer)
# Operations inside the loop:
# Heap: pop/push operations = O(logk), where k is the length of heap.
# Queue operations are O(1)
# Counter: O(m), where m is the number of tasks
# Overall: O(timer*logk) as the dominant time complexity.

# Space complexity:
# Overall, space complexity is O(n), where n is the number of unique tasks.

# Counter: Uses O(n) space to store the frequency of each unique task.
# Max Heap: Can hold up to n unique tasks, so its space complexity is O(n).
# Cooldown Queue: Similarly, the cooldown queue can hold up to n unique tasks, so it also uses O(n) space.


from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-val for val in freq.values()]
        heapq.heapify(max_heap)

        timer = 0
        cooldown = deque()
        while max_heap or cooldown:
            timer += 1

            if max_heap:
                task = -heapq.heappop(max_heap)
                if task > 1:
                    cooldown.append((task-1, timer + n))

            while cooldown and cooldown[0][1] == timer:
                heapq.heappush(max_heap, - cooldown.popleft()[0])

        return timer

