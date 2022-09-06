
import sys


import sys
def linear_search(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            return i
    return sys.maxsize

def search_in_range(nums, start, end, target):
    for i in range(start, end + 1):
        if target == nums[i]:
            return i
    return sys.maxsize


if __name__ == "__main__":

    nums = [3, 4, 6, 9, 10, 1, 5]
    print(linear_search(nums, 10))
    print(search_in_range(nums, 1, 3, 10))
