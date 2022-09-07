# Leetcode: https://leetcode.com/problems/longest-mountain-in-array/

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    max_len = 0
    for i in range(n):
        count = 0
        left = right = False
        k = m = i
        # Check for left side
        while k > 0 and nums[k] > nums[k - 1]:
            left = True
            count += 1
            k -= 1

            # Check for right side
        while m < n - 1 and nums[m] > nums[m + 1]:
            right = True
            count += 1
            m += 1
        if left and right:
            max_len = max(count + 1, max_len)
    print(max_len)