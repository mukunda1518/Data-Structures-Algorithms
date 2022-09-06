def peak_element(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return r # return l or r - both are same

if __name__ == "__main__":
    nums = input().split(" ")
    nums = list(map(int, nums))
    print(peak_element(nums))