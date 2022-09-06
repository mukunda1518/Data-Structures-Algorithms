def find_quadruplets(nums, n, target):
    count = 0
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n - 2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            rem_sum = target - (nums[i] + nums[j])
            k, m = j + 1, n - 1
            while k < m:
                if nums[k] + nums[m] < rem_sum:
                    k += 1
                elif nums[k] + nums[m] > rem_sum:
                    m -= 1
                else:
                    count += 1
                    res.append([nums[i], nums[j], nums[k], nums[m]])
                    k += 1 
                    while k < m and nums[k] == nums[k-1]:
                        k += 1 
                    m -= 1 
                    while m > k and nums[m] == nums[m + 1]:
                        m -= 1 
    print(count)

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    find_quadruplets(nums, n, k)