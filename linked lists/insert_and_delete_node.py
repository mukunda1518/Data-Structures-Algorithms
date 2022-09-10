class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        flag = True
        while temp:
            flag = False
            print(temp.data, end=" ")
            temp = temp.next
        if flag:
            print(-1)

    def insert_0_at_k_position(self, head, k):
        dummy_node, new_node = Node(0), Node(0)
        dummy_node.next = head
        temp = dummy_node

        for _ in range(k - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

        if head == new_node.next:
            head = new_node
        return head


    def delete_element_at_k_postion_method2(self, head, k):
        if k == 1:
            head = head.next
            return head
        dummy_node = Node(0)
        dummy_node.next = head
        temp = dummy_node
        for _ in range(k - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head

    def delete_element_at_k_postion_method1(self, head, k):
        prev = curr = head
        for _ in range(k - 1):
            prev = curr
            curr = curr.next
        if prev == curr:
            if not prev.next:
                head = None
            else:
                head = prev.next
        elif not curr:
            prev.next = None
        else:
            prev.next = curr.next
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

l_list.head = l_list.delete_element_at_k_postion_method2(l_list.head, k)
l_list.print_list()
