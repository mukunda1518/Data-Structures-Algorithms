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

    def remove_k_element(self, head, k):
        dummy = Node(-1)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.data == k:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next


# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
k = int(input())
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.remove_k_element(l_list.head, k)
l_list.print_list()
