count = 0

def lomuto_partion(nums, l, r):
    pivot = nums[r]
    i = l - 1
    global count
    for j in range(l, r):
        if nums[j] <= pivot:
            i += 1
            count += 1
            nums[i], nums[j] = nums[j], nums[i]
    count += 1
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

def quick_sort(nums, l, r):
    if l < r:
        pivot_index = lomuto_partion(nums, l, r)
        quick_sort(nums, l, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, r)

if __name__ == "__main__":
    # nums = [4, 6, 5, 2, 1, 3]
    # nums = [3, 1, 2]
    nums = [2, 4, 1, 3]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
    print(count)



class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1
    
    def quickSort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, high)

