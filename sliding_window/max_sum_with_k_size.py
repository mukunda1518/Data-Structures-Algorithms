if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    max_sum = 0
    sum_ = 0
    i, j = 0, 0
    while j < len(nums):
        sum_ += nums[j]
        if j - i + 1 < k:
            j += 1 
        elif j - i + 1 == k:
            max_sum = max(sum_, max_sum)
            sum_ -= nums[i]
            i += 1 
            j += 1
    print(max_sum)