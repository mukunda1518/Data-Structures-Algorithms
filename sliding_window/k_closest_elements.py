def get_k_closest_nums(nums, n, k, x):
    l = 0
    r = n - k
    while l < r:
        mid = l + (r - l) // 2
        if x <= nums[mid]:
            r = mid
        elif x >= nums[mid + k]:
            l = mid + 1
        else:
            if (nums[mid] + nums[mid + k]) // 2 < x:
                l = mid + 1
            else:
                r = mid
    for i in range(l, l + k):
        print(nums[i], end=" ")
    return


def get_k_closest_nums1_max(nums, n, k, x):
    l = 0
    r = n - k
    while l < r:
        mid = l + (r - l) // 2
        if x <= nums[mid]:
            r = mid
        elif x >= nums[mid + k]:
            l = mid + 1
        else:
            if (nums[mid] + nums[mid + k]) // 2 <= x:
                l = mid + 1
            else:
                r = mid
    for i in range(l, l + k):
        print(nums[i], end=" ")
    return


if __name__ == "__main__":
    n, k, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    get_k_closest_nums(nums, n, k, x)