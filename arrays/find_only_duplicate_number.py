# Leetcode: https://leetcode.com/problems/find-the-duplicate-number/submissions/

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    l, r = 1, n - 1
    while l < r:
        mid = l + (r - l) // 2
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if count <= mid:
            l = mid + 1
        else:
            r = mid
    print(l)
