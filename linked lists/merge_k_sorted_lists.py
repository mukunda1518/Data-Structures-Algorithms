
# Leetcode: https://leetcode.com/problems/merge-k-sorted-lists/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(list1, list2))
            lists = merged_lists

        return lists[0]   

    def mergeTwoLists(self, list1, list2):
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1 or list2:
            curr.next = list1 if list1 else list2
    
        return dummy.next
