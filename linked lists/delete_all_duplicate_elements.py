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
    
    def delete_all_duplicate_elements(self, head):
        dummy = Node(-1)
        dummy.next = head
        temp = dummy
        while temp.next:
            if temp.next.data == temp.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next

# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.delete_all_duplicate_elements(l_list.head)
l_list.print_list()
