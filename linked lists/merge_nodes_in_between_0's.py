# Leetcode Problem : https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Apporach1
        prev = head
        temp = head.next
        sum_ = 0
        while temp:
            sum_ += temp.val
            if temp.val == 0:
                temp.val = sum_
                prev.next = temp
                prev = temp
                sum_ = 0
            temp = temp.next
        return head.next
        
        
        # Apporach2
        dummy = ListNode(0)
        temp = dummy
        sum_= 0
        head = head.next
        while head:
            sum_ += head.val
            if head.val == 0:
                temp.next = ListNode(sum_)
                temp = temp.next
                sum_ = 0
            head = head.next
        return dummy.next