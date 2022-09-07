# Leetcode: https://leetcode.com/problems/count-number-of-nice-subarrays/

from collections import defaultdict

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    dict_ = defaultdict(int)
    prefix_sum = 0
    for i in range(n):
        if nums[i] % 2:
            nums[i] = 1
        else:
            nums[i] = 0

    for i in range(n):
        prefix_sum += nums[i]
        if prefix_sum == k:
            count += 1
        x = prefix_sum - k
        if x in dict_:
            count += dict_[x]
        dict_[prefix_sum] += 1
    print(count)

    # for i in range(n):
    #     odd = 0
    #     for j in range(i, n):
    #         if nums[j] % 2 == 1:
    #             odd += 1
    #             if odd == k:
    #                 count += 1
    #             if odd > k:
    #                 break
    #         elif odd == k and nums[j] % 2 == 0:
    #             count += 1
    # print(count)
