# Leetcode Problem : https://leetcode.com/problems/reverse-nodes-in-k-group/

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

    def reverse_every_k_consecutive_nodes_1(self, head, k):
        dummy = Node(-1)
        dummy.next = head
        prev_left = dummy
        right = head
        while right:
            k_count = k
            while k_count > 1 and right.next:
                right = right.next
                k_count -= 1 
            if k_count > 1:
                return dummy.next
            left = prev_left.next
            prev_left.next = right
            prev_left = left
            next_right = right.next
            prev = next_right
            while left != next_right:
                temp = left.next
                left.next = prev
                prev = left 
                left = temp
            right = left
        return dummy.next

    def reverse_every_k_consecutive_nodes(self, head, k):
        dummy = Node(-1, head)
        group_prev = dummy
        while True:
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            # reverse group 
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev= curr
                curr = temp
            
            temp = group_prev.next 
            group_prev.next = kth
            group_prev = temp
        return dummy.next
    
    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
k = int(input())
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
l_list.head = l_list.reverse_every_k_consecutive_nodes(l_list.head, k)
l_list.print_list()
