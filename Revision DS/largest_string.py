# GeeksforGeeks:  https://www.geeksforgeeks.org/largest-string-obtained-in-dictionary-order-after-deleting-k-characters/


from collections import deque


# Time Limit Exceed Solution
def get_all_subsequence_strings(s, k):
    all_subsequence_strings = []
    n = len(s)
    m = n - k

    def get_subsequences_of_string(up_s, s):
        if len(up_s) == m:
            all_subsequence_strings.append(up_s)
            return
        if len(s) == 0:
            return
        get_subsequences_of_string(up_s + s[0], s[1:])
        get_subsequences_of_string(up_s, s[1:])

    get_subsequences_of_string("", s)
    all_subsequence_strings.sort()
    print(all_subsequence_strings[-1])


def using_deque(s, k):
    dq = deque()
    for char in s:
        while dq and dq[-1] < char and k > 0:
            dq.pop()
            k -= 1
        dq.append(char)
    while k:  # s = zzzz and  k = 1
        dq.pop()
        k -= 1

    print("".join(dq))


if __name__ == "__main__":
    k = int(input())
    s = input()
    # get_all_subsequence_strings(s, k)
    using_deque(s, k)
