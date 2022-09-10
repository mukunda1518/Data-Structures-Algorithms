class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_multiples_of_7(self):
        temp = self.head
        flag = True
        while temp:
            data = temp.data
            if data % 7 == 0:
                flag = False
                print(data, end=" ")
            temp = temp.next
        if flag:
            print(-1)


# main
nums = list(map(int, input().split()))
nums.pop()
l_list = LinkedList()
l_list.head = Node(nums[0])
temp = l_list.head
for num in nums[1:]:
    temp.next = Node(num)
    temp = temp.next
l_list.print_multiples_of_7()


