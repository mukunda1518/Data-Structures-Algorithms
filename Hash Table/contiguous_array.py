# Leetcode: https://leetcode.com/problems/contiguous-array/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        prefix_sum = {}
        prefix_sum[0] = -1
        max_len = 0
        for i in range(len(nums)):
            count += -1 if nums[i] == 0 else 1 
            if count in prefix_sum:
                value = i - prefix_sum[count]
                max_len = max(value, max_len)
            else:
                prefix_sum[count] = i 
        return max_len


# To find no of such subarrays both 1's and 0's are equal
# https://www.youtube.com/watch?v=svMdY6wlQ6I

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    count_dict = {}
    count_dict[0] = 0
    for i in range(len(nums)):
        count += -1 if nums[i] == 0 else 1 
        if count in count_dict:
            count_dict[count] += count_dict[count] + 1
        else:
            count_dict[count] = 0 
    print(count_dict)
    total_count = sum(list(count_dict.values()))
    print(total_count)