# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:

        # Apporach1 - Time Complexity: O(n) - Space Complexity: O(1)

        slow = fast = head

        # Find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        # Apporach2 - Time Complexity: O(n) - Space Complexity: O(n)

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True