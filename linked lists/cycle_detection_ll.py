# Leetcode: https://leetcode.com/problems/linked-list-cycle/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

        ### Approach
        # if head is None:
        #     return False
        # temp = head
        # nodes = []
        # while temp.next and temp not in nodes:
        #     nodes.append(temp)
        #     temp = temp.next
        # if temp.next is None:
        #     return False
        # else:
        #     return True
        