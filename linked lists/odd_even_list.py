# Leetcode Problem Link: https://leetcode.com/problems/odd-even-linked-list/

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

    def odd_even_list(self, head):
        # Here dummy1.next and dummy2.next will store the head of odd and even list
        dummy1 = odd = Node(0)
        dummy2 = even = Node(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        # join the evn tail to odd list end
        odd.next = dummy2.next
        return dummy1.next

        # Second Apporach
        # oddhead = odd = Node(0)
        # evenhead = even = Node(0)
        # while head:
        #     if i % 2 == 1:
        #         odd.next = head
        #         odd = odd.next
        #     else:
        #         even.next = head
        #         even = even.next
        #     i += 1
        #     head = head.next
        # even.next = None
        # odd.next = evenhead.next
        # return oddhead.next


# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next

ans = LinkedList()
ans.head = ans.odd_even_list(l_list.head)
ans.print_list()
