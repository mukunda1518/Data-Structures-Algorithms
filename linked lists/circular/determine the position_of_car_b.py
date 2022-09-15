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

    def get_car_b_position(self, a_speed, b_speed):
        temp_a = temp_b = self.head
        while temp_a.next != self.head:
            j = 0
            while j < a_speed and temp_a.next != self.head:
                j += 1
                temp_a = temp_a.next
            k = b_speed if j == a_speed and temp_a.next != self.head else min(j, b_speed)
            for _ in range(k):
                temp_b = temp_b.next
        return temp_b.data


# main

l_list = CircularLinkedList()
nums = [int(val) for val in input().split()]
nums.pop()
a_speed, b_speed = map(int, input().split())
l_list.head = Node(nums[0])
temp = l_list.head
for val in nums[1:]:
    temp.next = Node(val)
    temp = temp.next
temp.next = l_list.head
print(l_list.get_car_b_position(a_speed, b_speed))

