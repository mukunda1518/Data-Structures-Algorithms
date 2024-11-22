# Leetcode: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curr_sum = 0
        nums_set = set()
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while r - l + 1 > k or nums[r] in nums_set:
                curr_sum -= nums[l]
                nums_set.remove(nums[l])
                l += 1

            if r - l + 1 == k:
                res = max(res, curr_sum)

            nums_set.add(nums[r])

        return res


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    k = int(input())
    print(Solution().maximumSubarraySum(nums, k))
    