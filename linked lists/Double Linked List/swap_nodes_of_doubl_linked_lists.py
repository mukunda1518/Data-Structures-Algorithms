class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def swap_nodes(self, head, tail, k):
        if head.next == None:
            return head, tail
        k1, k2 = head, tail
        for _ in range(1, k):
            k1 = k1.next
            k2 = k2.prev
        if k1 == k2:
            return head, tail
        # if we have to swap head and tail nodes 
        if k1.prev == None or k1.next == None:
            temp = head
            # if there are only 2 nodes 
            if head.next == tail:
                head.next = None
                head.prev = tail
                tail.prev = None
                tail.next = head
                head, tail = tail, temp
                return head, tail
            tail.next = head.next
            head.prev = tail.prev
            
            tail.prev.next = head
            head.next.prev = tail
            
            head.next, tail.prev = None, None
            return tail, head
        # If nodes are not head and tail but consecutive
        if k1.next == k2 or k1.prev == k2:
            if k1.next == k2:
                k1.next = k2.next
                k1.next.prev = k1
                
                k2.next = k1
                k1.prev.next = k2
                
                k2.prev = k1.prev
                k1.prev = k2
            else:
                k2.next = k1.next
                k1.next.prev = k2
                
                k1.next = k2
                k2.prev.next = k1 
                
                k1.prev = k2.prev
                k2.prev = k1
            return head, tail
        
        # if nodes are not consecutive
        k1_prev, k1_next = k1.prev, k1.next
        k2_prev, k2_next = k2.prev, k2.next
        
        k1.prev.next = k2 
        k1.next.prev = k2 
        k2.prev.next = k1 
        k2.next.prev = k1 
        k1.prev, k1.next = k2_prev, k2_next
        k2.prev, k2.next = k1_prev, k1_next
        return head, tail
                
    
    def swap_nodes_1(self, k):
        i = 1
        left = self.head
        right = self.tail
        while i < k:
            left = left.next
            right = right.prev
            i += 1 
        left.data, right.data = right.data, left.data
   
# main

l_list = DoubleLinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
k = int(input())
l_list.head = Node(nums[0])
curr = l_list.head
prev = None
for val in nums[1:]:
    curr.prev = prev
    curr.next = Node(val)
    curr.next.prev = curr
    prev = curr
    curr = curr.next
l_list.tail = curr
l_list.head, l_list.tail = l_list.swap_nodes(l_list.head, l_list.tail, k)
l_list.print_list()
