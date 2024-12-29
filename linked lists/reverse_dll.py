#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        temp = head
        
        while temp.next:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        temp.prev, temp.next = temp.next, temp.prev
        return temp
