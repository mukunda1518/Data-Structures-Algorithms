class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
    def get_max_three_consecutive_nodes_sum(self):
        max_sum = 0
        sum_ = 0
        left = right = self.head
        j = 0
        while True:
            sum_ += right.data
            j += 1 
            if j == 3:
                max_sum = max(max_sum, sum_)
                sum_ -= left.data
                left = left.next
                j -= 1
                if left == self.head:
                    break
            right = right.next
        return max_sum

# main

l_list = LinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
temp.next = l_list.head
print(l_list.get_max_three_consecutive_nodes_sum())
