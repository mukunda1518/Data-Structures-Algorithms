def swaps_in_array(nums, order_nums, n):
    swaps = 0
    for i in range(n):
        if nums[i] == order_nums[i]:
            continue
        index = order_nums.index(nums[i])
        order_nums[i], order_nums[index] = order_nums[index], order_nums[i]
        swaps += 1
    return swaps


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    asc_nums = list(range(1, n + 1))
    desc_nums = list(range(n, 0, -1))

    asc_swaps = swaps_in_array(nums[:], asc_nums, n)
    desc_swaps = swaps_in_array(nums[:], desc_nums, n)
    print(min(asc_swaps, desc_swaps))