# Leetcode: https://leetcode.com/problems/implement-stack-using-queues/description/


from collections import deque


# Using Single Queue
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        size = len(self.queue)
        for _ in range(size - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Using Multiple Queues
class MyStack1:

    def __init__(self):
        self.queue = []
        self.queue1 = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.queue1.append(self.queue.pop(0))
        val = self.queue.pop()
        self.queue, self.queue1 = self.queue1, self.queue
        return val

    def top(self) -> int:
        while len(self.queue) > 1:
            self.queue1.append(self.queue.pop(0))
        val = self.queue.pop()
        self.queue1.append(val)
        self.queue, self.queue1 = self.queue1, self.queue
        return val

    def empty(self) -> bool:
        return not self.queue
