# Leetcode Question : https://leetcode.com/problems/palindrome-linked-list/

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
    
    def is_linked_list_palindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while right:
            if left.data != right.data:
                return "NO"
            left = left.next
            right = right.next
        return "YES"

# main

t = int(input())
for _ in range(t):
    l_list = LinkedList()
    nums = [int(val) for val in input().split()]
    nums.pop()
    l_list.head = Node(nums[0])
    temp = l_list.head
    for val in nums[1:]:
        temp.next = Node(val)
        temp = temp.next
    print(l_list.is_linked_list_palindrome(l_list.head))
    




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp:
            next_temp = temp.next
            temp.next = prev
            prev = temp
            temp = next_temp
        return prev 

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = self.reverse(slow.next)

        left = head
        right = new_head

        while right:
            if left.val != right.val:
                self.reverse(new_head)
                return False
            left = left.next
            right = right.next
        self.reverse(new_head)
        return True
