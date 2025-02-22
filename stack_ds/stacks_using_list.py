


class Stack:
    
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())
    stack.push(6)
    print(stack.top())
    print(stack.size())
    