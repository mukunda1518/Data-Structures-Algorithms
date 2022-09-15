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

    def rotate_right_k_times(self, head, k):
        count = 1
        tail = head
        while tail.next:
            count += 1
            tail = tail.next
        if k % count == 0:
            return head
        k = k % count
        r = count - k

        temp = head
        for _ in range(r - 1):
            temp = temp.next
        tail.next = head
        head = temp.next
        temp.next = None
        return head


# main

l_list = LinkedList()
k = int(input())
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.rotate_right_k_times(l_list.head, k)
l_list.print_list()
