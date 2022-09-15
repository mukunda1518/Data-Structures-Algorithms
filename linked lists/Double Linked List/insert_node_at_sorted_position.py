class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def insert_node_at_sorted_position(self, k):
        new_node = Node(k)
        if k >= self.tail.data:
            new_node.prev = self.tail
            self.tail.next = new_node
            return self.head, self.tail
        curr = self.head
        while curr:
            if k <= curr.data:
                if curr.prev == None:
                    self.head = new_node
                else:
                    curr.prev.next = new_node
                break
            curr = curr.next
        new_node.prev = curr.prev
        new_node.next = curr
        curr.prev = new_node
        return self.head, self.tail
            


# main

l_list = DoubleLinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
k = int(input())
l_list.head = Node(nums[0])
curr = l_list.head
prev = None
for val in nums[1:]:
    curr.prev = prev
    curr.next = Node(val)
    curr.next.prev = curr
    prev = curr
    curr = curr.next
l_list.tail = curr
l_list.head, l_list.tail = l_list.insert_node_at_sorted_position(k)
l_list.print_list()
