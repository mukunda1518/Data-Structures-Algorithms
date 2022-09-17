# Leetcode: https://leetcode.com/problems/partition-list/


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

    def partition_linked_list(self, head, k):
        lesser = lesser_head = Node(-1)
        greater = greater_head = Node(-1)
        curr = head
        while curr:
            if curr.data < k:
                lesser.next = curr
                lesser = lesser.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        lesser.next = greater_head.next
        greater.next = None
        return lesser_head.next
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
l_list.head = l_list.partition_linked_list(l_list.head, k)
l_list.print_list()
