



class QueueUsingStack:  # Dequeue costly
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, element):    # Time Complexity : O(1)
        self.stack1.append(element)

    def dequeue(self):    # Time Complexity : O(n)
        if not self.stack1 and not self.stack2:
            return "Queue is empty"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):    # Time Complexity : O(n)
        if not self.stack1 and not self.stack2:
            return "Queue is empty"

        if not self.stack2:
            while not self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def size(self):    # Time Complexity : O(n)
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):     # Time Complexity : O(1)
        return not self.stack1 and not self.stack2



class QueueUsingStack1:  # Enqueue costly
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(element)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            return "Queue is empty"
        return self.stack1.pop()

    def peek(self):
        if not self.stack1:
            return "Queue is empty"
        return self.stack1[-1]

    def size(self):
        return len(self.stack1)

    def is_empty(self):
        return not self.stack1

if __name__ == "__main__":
    queue = QueueUsingStack()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.peek())
    print(queue.size())
    print(queue.is_empty())
    print("---------")
    queue = QueueUsingStack1()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # print(queue.dequeue())
    # print(queue.dequeue())
    print(queue.peek())
    print(queue.size())
    print(queue.is_empty())
        
        

    
    
    