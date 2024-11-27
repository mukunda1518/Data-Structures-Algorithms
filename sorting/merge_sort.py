
# Leetcode - https://leetcode.com/problems/sort-an-array/submissions/1463914939/


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1: return nums
    
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
    
        result = []
        l, r = 0, 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        if l < len(left):
            result.extend(left[l:])
        elif r < len(right):
            result.extend(right[r:])

        return result


def merge(left, right):
    len_l = len(left)
    len_r = len(right)
    i = 0
    res = []
    l, r = 0, 0
    while i < len_l + len_r:
        i += 1
        if r >= len_r or (l < len_l and left[l] <= right[r]):
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    return res


def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    left = merge_sort(nums[0:n // 2])
    right = merge_sort(nums[n // 2:n])
    return merge(left, right)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    s = merge_sort(nums)
    print(s)

