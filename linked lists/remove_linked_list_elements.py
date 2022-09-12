# Leetcode Question :https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val: int):

        # Approach1
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

        # Approach2

        prev = curr = head
        while curr:
            if curr.val == val:
                if head == curr and curr == prev:
                    head = head.next
                    prev = head
                    curr = head
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head