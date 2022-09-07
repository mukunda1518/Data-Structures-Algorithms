# Leetcode: https://leetcode.com/problems/subarray-product-less-than-k/

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    i = 0
    prod = 1
    count = 0
    for j in range(n):
        prod *= nums[j]
        while i <= j and prod >= k:
            prod = prod // nums[i]
            i += 1
        count += j - i + 1
        j += 1
    print(count)
