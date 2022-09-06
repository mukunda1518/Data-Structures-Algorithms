def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        curr_num = nums[i]
        j = i - 1
        while j >= 0 and curr_num < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = curr_num


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    insertion_sort(nums)
    print(*nums)