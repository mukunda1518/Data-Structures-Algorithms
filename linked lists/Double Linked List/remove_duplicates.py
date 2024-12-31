# Problem: https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        temp = head
        
        while temp:
            
            next_node = temp.next
            
            while next_node and next_node.data == temp.data:
                next_node = next_node.next
            
            temp.next = next_node
            if next_node:
                next_node.prev = temp
            
            temp = temp.next
        
        return head