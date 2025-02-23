
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.size += 1

    def dequeue(self):
        if self.start is None:
            return "Queue Empty"
        data = self.start.data
        self.start = self.start.next
        self.size -= 1
        return data

    def peek(self):
        if self.start is None:
            return "Queue Empty"
        return self.start.data
    
    def len(self):
        return self.size


        
class MyQueue:
    
    def __init__(self):
        self._front = None
        self._rear = None
    #Function to push an element into the queue.
    def push(self, item):
        new_node = Node(item)
        if not self._front and not self._rear:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
    
    #Function to pop front element from the queue.
    def pop(self):
        if not self._front:
            return -1
        val = self._front.data
        self._front = self._front.next
        if not self._front:
            self._rear = None
        return val




if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.len())
