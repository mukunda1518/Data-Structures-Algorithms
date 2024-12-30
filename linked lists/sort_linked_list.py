# Leetcode: https://leetcode.com/problems/sort-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeLists(self, list1, list2):
        dummy_node = ListNode(-1)
        temp = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy_node.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.findMiddle(head)
        right = middle.next
        left = head
        middle.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeLists(left, right)
