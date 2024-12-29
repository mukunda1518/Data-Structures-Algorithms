class Solution:
    def delete_node(self, head, x):
        #code here
        temp = head
        count = 0
        while temp:
            count += 1
            if count == x:
                break
            temp = temp.next
            
        prev_node = temp.prev
        next_node = temp.next

        if prev_node is None and next_node is None:
            return None
        elif prev_node is None: # head
            head.next = None
            head = next_node
            head.prev = None
            return head
        elif next_node is None: # Last Node
            prev_node.next = None
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
        return head
