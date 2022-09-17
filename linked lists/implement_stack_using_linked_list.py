class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:

    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return False if self.root else True
    
    def push(self, data):
        new_node = Node(data)
        if self.root:
            new_node.next = self.root
            self.root = new_node
        else:
            self.root = new_node

    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.root.data)
            self.root = self.root.next
        

# main 
n = int(input())
nums = list(map(int, input().split()))
s = Stack()
i = 0
q = 0
while q < n:
    if nums[i] == 1:
        data = nums[i+1]
        s.push(data)
        i += 2
    elif nums[i] == 2:
        s.pop()
        i += 1 
    q += 1


