# Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    sum_ = 0
    count = 0
    map_ = {0: 1}
    for num in nums:
        sum_ += num
        if sum_ - k in map_:
            count += map_[sum_ - k]
        if sum_ not in map_:
            map_[sum_] = 1 
        else:
            map_[sum_] += 1 
    print(count)
            