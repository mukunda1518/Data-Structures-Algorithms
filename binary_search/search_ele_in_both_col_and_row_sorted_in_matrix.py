def search_matrix(nums, target):
    r = 0
    c = len(nums[0]) - 1
    while r < len(nums) and c >= 0:
        if nums[r][c] == target:
            return (r, c)
        elif nums[r][c] > target:
            r += 1
        else:
            c -= 1
    return (-1, -1)


if __name__ == "__main__":
    nums = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [28, 29, 37, 49],
        [33, 34, 38, 50]    
    ]
    target = 38
    print(search_matrix(nums, target)) 