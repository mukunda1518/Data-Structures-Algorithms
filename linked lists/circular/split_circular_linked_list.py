class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
    
    def split_circular_linked_list(self):
        slow = fast = self.head
        flag = True
        if fast.next == self.tail:
            flag = False
        while flag:
            slow = slow.next
            fast = fast.next.next
            if fast == self.tail or fast.next == self.tail:
                break
        temp = slow.next
        slow.next = self.head
        self.tail.next = temp
        return self.head, temp

# main

l_list = CircularLinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
temp.next = l_list.head
l_list.tail = temp

first_list = CircularLinkedList()
second_list = CircularLinkedList()
first_list.head, second_list.head = l_list.split_circular_linked_list()
first_list.print_list()
print()
second_list.print_list()
