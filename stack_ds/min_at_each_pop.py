from collections import deque

initial_stack = deque()
min_stack = deque()


def push_to_stack(nums, n):
    initial_stack.append(nums[0])
    min_stack.append(nums[0])

    for i in range(1, n):
        if nums[i] <= min_stack[-1]:
            min_stack.append(nums[i])
        initial_stack.append(nums[i])


def get_min_in_pop():
    while initial_stack:
        print(min_stack[-1], end=" ")
        if min_stack[-1] == initial_stack[-1]:
            min_stack.pop()
            initial_stack.pop()
        else:
            initial_stack.pop()


# main()
n = int(input())
nums = list(map(int, input().split()))
push_to_stack(nums, n)
get_min_in_pop()