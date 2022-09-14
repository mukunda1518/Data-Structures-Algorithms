
# Starting from 1st node delete m nodes until 1 node remains

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
 
    def get_last_person(self, m):
        prev = curr = self.head
        j = 0
        while True:
            j += 1
            if j == m:
                prev.next = curr.next
                curr = curr.next
                j = 0
                if prev == curr:
                    return prev.data
            else:
                prev = curr
                curr = curr.next
    
def get_josephus_position(n, m):
    head = Node(1)
    temp = head
    for i in range(2, n + 1):
        temp.next = Node(i)
        temp = temp.next
    temp.next = head
    
    prev = head
    curr = head
    while curr.next != curr: # using prev or curr is fine because curr == prev
        count = 1 
        while count != m:
            prev = curr
            curr = curr.next
            count += 1 
        prev.next = curr.next
        curr = prev.next
    return curr.data
    
# main

n, m = map(int, input().split())
print(get_josephus_position(n, m))
# l_list = CircularLinkedList()
# nums = [i for i in range(1, n + 1)]
# l_list.head = Node(nums[0])
# temp = l_list.head
# for val in nums[1:]:
#     temp.next = Node(val)
#     temp = temp.next
# temp.next = l_list.head
# print(l_list.get_last_person(m))
