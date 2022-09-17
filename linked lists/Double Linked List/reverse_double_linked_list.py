class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            curr.prev = temp
            prev = curr
            curr = temp
        self.head = prev
    
    def push(self, new_data):
        new_node = Node(new_data)
        last = self.head
        new_node.next = None
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last


# main

dll = DoubleLinkedList()
nums = [int(val) for val in input().split()]
i = 0
while nums[i] != -1:
    dll.push(nums[i])
    i += 1 
dll.reverse()
dll.print_list()
