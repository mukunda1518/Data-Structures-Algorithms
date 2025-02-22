from collections import deque
def check_palindrome(str_):
    dq = deque(str_)
    while len(dq) > 1:
        front = dq[0]
        rare = dq[-1]
        if front != rare:
            return "No"
        dq.popleft()
        dq.pop()
    return "Yes"
   
if __name__ == "__main__":
    t = int(input())
    strings = [input() for _ in range(t)]
    for str_ in strings:
        print(check_palindrome(str_))