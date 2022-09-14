# Leetcode problem : https://leetcode.com/problems/add-two-numbers/

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

    def add_two_numbers(self, l1, l2):
        dummy = curr = Node(0)
        carry = 0
        l1 = l_list_a.head
        l2 = l_list_b.head
        
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.data
                l1 = l1.next
            if l2:
                val2 = l2.data
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            curr.next = Node(val)
            curr = curr.next
        return dummy.next
    
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


l_list_c = LinkedList()
l_list_c.head = LinkedList().add_two_numbers(l_list_a, l_list_b)
l_list_c.print_list()
        