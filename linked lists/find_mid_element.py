# Leetcode Question: https://leetcode.com/problems/middle-of-the-linked-list/submissions/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_middle_element(self):
        fast = slow = self.head
        # find middle (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)


# main
l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head

for num in nums[1:]:
    temp.next = Node(num)
    temp = temp.next
l_list.get_middle_element()

