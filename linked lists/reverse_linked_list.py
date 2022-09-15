class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse_linked_list(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.reverse_linked_list(l_list.head)
l_list.print_list()
