

class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    
    def __init__(self):
        self.top = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        new_node = StackNode(data)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    #Function to remove an item from top of the stack.
    def pop(self):
        if not self.top:
            return -1
        val = self.top.data
        self.top = self.top.next
        return val
