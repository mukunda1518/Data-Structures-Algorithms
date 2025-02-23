class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rare = -1
    
    def enqueue(self, x):
        if self.front == -1:
            self.front = 0
        self.rare += 1
        self.queue.append(x)
    
    def is_empty(self):
        if self.front > self.rare or self.front == -1:
            return True
        return False
    
    def dequeue(self):
        if self.is_empty():
            print("-1", end = " ")
        else:
            print(self.queue[self.front], end = " ")
            self.front += 1

# main 

n = int(input())
obj = Queue()
for _ in range(n):
    oper = input().split()
    if oper[0] == "A":
        obj.enqueue(int(oper[1]))
    elif oper[0] == "B":
        obj.dequeue()
