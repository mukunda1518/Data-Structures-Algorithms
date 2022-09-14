class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("-1")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    @staticmethod
    def merge_linked_list_alternatively(head_a, head_b):
        temp_a = head_a
        temp_b = head_b
        while temp_a and temp_b:
            temp = temp_a.next
            temp_a.next = temp_b
            temp_b = temp_b.next
            temp_a.next.next = temp
            temp_a = temp
        return head_a, temp_b

# main

nums_a = [int(val) for val in input().split()]
nums_a.pop()
nums_b = [int(val) for val in input().split()]
nums_b.pop()    

l_list_a = LinkedList()
l_list_a.head = Node(nums_a[0])
temp_a = l_list_a.head
for val in nums_a[1:]:
    temp_a.next = Node(val)
    temp_a = temp_a.next

l_list_b = LinkedList()
l_list_b.head = Node(nums_b[0])
temp_b = l_list_b.head
for val in nums_b[1:]:
    temp_b.next = Node(val)
    temp_b = temp_b.next

l_list_a.head, l_list_b.head = LinkedList().merge_linked_list_alternatively(l_list_a.head, l_list_b.head)
l_list_a.print_list()
print()
l_list_b.print_list()
    