def selection_sort(nums):
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    selection_sort(nums)
    print(*nums)
