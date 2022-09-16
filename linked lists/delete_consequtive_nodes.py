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

    def delete_k_consecutive_nodes(self, m, k):
        temp_m = self.head
        while temp_m and temp_m.next:
            j = 1 
            while j < m and temp_m.next:
                j += 1 
                temp_m = temp_m.next
            i = 0
            temp_n = temp_m
            while i < k and temp_n.next:
                i += 1 
                temp_n = temp_n.next
            temp_m.next = temp_n.next
            temp_m = temp_m.next
            
    def delete_k_consecutive_nodes_1(self, m, k):
        curr_node = m_last_node = self.head
        while curr_node:
            m_count, k_count = m, k 
            while curr_node != None and m_count != 0:
                m_last_node = curr_node
                curr_node = curr_node.next
                m_count -= 1 
            while curr_node != None and k_count != 0:
                curr_node = curr_node.next
                k_count -= 1 
            m_last_node.next = curr_node
# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
m, k = map(int, input().split())
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.delete_k_consecutive_nodes_1(m, k)
l_list.print_list()
