# Leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev, first = dummy, head
        second = first.next
        while first and first.next:
            # save pairs
            temp = first.next.next
            second = first.next
            
            # Swap pairs
            temp = second.next
            second.next, first.next = first, temp
            prev.next = second
            
            # update pointers
            prev = first
            first = temp
        return dummy.next