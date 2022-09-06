def order_agnostice_binary_search(nums, target, is_asc):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid 

        if is_asc:
            if nums[mid] < target:
                l = mid - 1
            else:
                r = mid + 1
        else:
            if nums[mid] < target:
                r = mid - 1
            else:
                l = mid + 1
    return -1

if __name__ == "__main__":
    nums = input().split(" ")
    target = int(input())
    nums = list(map(int, nums))
    is_asc = nums[0] > nums[-1]
    print(order_agnostice_binary_search(nums, target, is_asc))