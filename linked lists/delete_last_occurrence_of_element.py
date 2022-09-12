class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        if not self.head:
            print(-1)

    def delete_last_occurrence_of_k_element(self, head, k):
        curr = head
        res = prev = None
        while curr:
            if curr.data == k:
                res = prev
            prev = curr
            curr = curr.next
        if not res:
            return head.next
        res.next = res.next.next
        return head


# main
l_list = LinkedList()
nums = [int(val) for val in input().split()]
k = int(input())
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.delete_last_occurrence_of_k_element(l_list.head, k)
l_list.print_list()
