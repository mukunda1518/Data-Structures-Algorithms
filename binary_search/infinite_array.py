def binary_search(nums, l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            l = mid - 1
        else:
            r = mid + 1
    return -1

def get_ans(nums, target):
    start = 0
    end = 1
    while target > end:
        start, end = end + 1, end + (end - start + 1) * 2
    return binary_search(nums, start, end, target)
    

if __name__ == "__main__":
    nums = input().split(" ")
    target = int(input())
    nums = list(map(int, nums))
    print(get_ans(nums, target))
