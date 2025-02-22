


class Queue:
    def __init__(self):
        self.queue = []
        self._start = -1
        self._end = -1

    def is_empty(self):
        if self._start > self._end or self._start == -1:
            return True
        return False

    def enqueue(self, x):
        if self._start == -1:
            self._start = 0
        self.queue.append(x)
        self._end += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self._start += 1
    
    # This is O(n) as it needs to shift elements
    # Can be used when we are not having start and end and also when we need to clear the elements from the memory
    def dequeue1(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            print("Queue is empty")      
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue[self._start])

    def rear(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue[self._end])

    def size(self):
        return self._end - self._start


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    queue.front()
    queue.rear()
    queue.size()

