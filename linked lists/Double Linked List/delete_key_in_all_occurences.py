#  Problem : https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1


class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        temp = head

        while temp:
            if temp.data == x:
                if temp == head:
                    head = temp.next
                next_node = temp.next
                prev_node = temp.prev
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                temp = next_node
            else:
                temp = temp.next
        return head
