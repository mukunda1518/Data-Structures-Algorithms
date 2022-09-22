# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        meeting_node = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meeting_node = slow
                break
        if not meeting_node:
            return None
        curr = head
        while curr != meeting_node:
            curr = curr.next
            meeting_node = meeting_node.next
        return curr
        
        