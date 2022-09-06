from functools import cmp_to_key
import math

global m


def modulus(i):
    val = math.fmod(i, m)
    return val


def compare(a, b):
    x = modulus(a)
    y = modulus(b)
    a_c = a & 1  # check is odd
    b_c = b & 1  # check is odd

    if x != y:
        return (x > y) - (x < y)  # default decending order
    elif a_c == 1 and b_c == 0:
        return -1
    elif a_c == 0 and b_c == 1:
        return 1
    elif a_c == 0 and b_c == 0:
        return (a > b) - (a < b)
    elif a_c == 1 and b_c == 1:
        return (a < b) - (a > b)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums, key=cmp_to_key(compare))
print(*nums)

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     nums = list(map(int, input().split()))
#     dict_a = {}
#     for i in range(-(m - 1), m):
#         dict_a[i] = {"even": [], "odd": []}
#     for num in nums:
#         rem = -(-(num) % m) if num < 0 else num % m
#         if num % 2 == 0:
#             dict_a[rem]["even"].append(num)
#         else:
#             dict_a[rem]["odd"].append(num)

#     modulo_nums = []
#     for value in dict_a.values():
#         odd = sorted(value["odd"], reverse=True)
#         even = sorted(value["even"])
#         modulo_nums.extend(odd)
#         modulo_nums.extend(even)
#     print(*modulo_nums)
