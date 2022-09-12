class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linked_list(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def delete_kth_element(self, head, k):
        dummy = Node(0)
        dummy.next = head
        temp = dummy
        for _ in range(k - 1):
            temp = temp.next
        if temp.next == head:
            head = temp.next.next
        temp.next = temp.next.next
        return head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        if self.head == None:
            print(-1)

    def remove_kth_node_from_end(self, head, k):
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# main
l_list = LinkedList()
nums = [int(val) for val in input().split()]
k = int(input())
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head

for num in nums[1:]:
    temp.next = Node(num)
    temp = temp.next

l_list.head = l_list.remove_kth_node_from_end(l_list.head, k)
l_list.print_list()

