def sorted_push(s, element):
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sorted_push(s, element)
        s.append(temp)


def sorted_stack(s):
    if len(s) != 0:
        temp = s.pop()
        sorted_stack(s)
        sorted_push(s, temp)


def print_stack(s):
    if len(s) == 0:
        return
    else:
        x = s[-1]
        s.pop(-1)
        print(x, end=" ")
        print_stack(s)
        s.append(x)


# main
stack = []
n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    stack.append(num)
sorted_stack(stack)
print_stack(stack)
