# Leetcode : https://leetcode.com/problems/move-zeroes/description/

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    i = 0
    for j in range(0, n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    print(*nums)