# Leetcode: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        curr = dummy_node
        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1 or temp2:
            sum_ = carry
            if temp1:
                sum_ += temp1.val
                temp1 = temp1.next
            if temp2:
                sum_ += temp2.val
                temp2 = temp2.next

            curr.next = ListNode(sum_ % 10)
            carry = sum_ // 10
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy_node.next
        