class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def EnQueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.rear = new_node
            self.front= new_node
    
    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False

    def DeQueue(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

# main 
nums = list(map(int, input().split()))
nums.pop()
n = len(nums)
q = Queue()
i = 0
while i < n:
    if nums[i] == 1:
        data = nums[i+1]
        q.EnQueue(data)
        i += 2
    elif nums[i] == 2:
        q.DeQueue()
        i += 1 