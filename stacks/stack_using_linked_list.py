

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
        
    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1 
    
    def peek(self):
        if self.is_empty():
            return "Stack Empty"
        return self.top.data

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def len(self):
        return self.size

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.len())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.len())
        
    