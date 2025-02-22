



class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def rear(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)



class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, element):    # Time Complexity : O(n)
        self.queue.enqueue(element)
        size = self.queue.size()
        for _ in range(size - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):  # Time Complexity : O(1)
        return self.queue.dequeue()

    def top(self):  # Time Complexity : O(1)
        return self.queue.front()

    def size(self):  # Time Complexity : O(1)
        return self.queue.size()


if __name__ == "__main__":
    stack = StackUsingQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.top())
    print(stack.size())