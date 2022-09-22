# Leetcode: https://leetcode.com/problems/happy-number/

def happy_number(num):
    set_a = set()
    while num != 1:
        sum_ = 0
        while num != 0:
            sum_ += (num % 10)**2
            num //= 10
        if sum_ in set_a:
            return "Not a Happy Number"
        set_a.add(sum_)
        num = sum_
    return "Happy Number"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num = int(input())
        print(happy_number(num))
    