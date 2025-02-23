from collections import deque


class Stack:
    def __init__(self):
        self.queue = deque()
    
    def push(self, element):    # Time Complexity : O(n)
        self.queue.append(element)
        size = len(self.queue)
        for _ in range(size - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):  # Time Complexity : O(1)
        if self.is_empty():
            return "Stack is empty"
        return self.queue.popleft()

    def top(self):  # Time Complexity : O(1)
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):  # Time Complexity : O(1)
        return len(self.queue) == 0

    def size(self):  # Time Complexity : O(1)
        return len(self.queue)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.top())
    print(stack.is_empty())
    print(stack.size())