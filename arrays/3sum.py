# Leetcode: https://leetcode.com/problems/3sum/

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums)
    triplets = []
    for i in range(n - 2):
        if i != 0 and nums[i - 1] == nums[i]:
            continue
        rem_sum = k - nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s > rem_sum:
                r -= 1
            elif s < rem_sum:
                l += 1
            else:
                if r < n - 1 and nums[l - 1] == nums[l] and nums[r] == nums[r + 1]:
                    r -= 1
                    l += 1
                    continue
                triplets.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
    if triplets:
        for triplet in triplets:
            print(*triplet)
    else:
        print("No triplets found")
