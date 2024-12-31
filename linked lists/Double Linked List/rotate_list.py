# Leetcode: https://leetcode.com/problems/rotate-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        len_ = 1
        tail = head
        while tail.next:
            len_ += 1
            tail = tail.next
        if k % len_ == 0:
            return head
        k = k % len_
        tail.next = head

        nth_node = len_ - k
        temp = head
        while nth_node > 1:
            nth_node -= 1
            temp = temp.next
        
        head = temp.next
        temp.next = None
        head.prev = None
        return head

        