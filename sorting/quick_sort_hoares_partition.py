asc_count = 0
desc_count = 0
def hoares_partition(nums, l, r):
    pivot = nums[l]
    i = l
    j = r 
    while True:
        while nums[i] < pivot:
            i += 1 
        while nums[j] > pivot:
            j -= 1 
        
        if i < j:
            global asc_count
            asc_count += 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            return j 
        i += 1 
        j -= 1

def quick_sort(nums, l, r):
    if l < r:
        pivot = hoares_partition(nums, l, r)
        quick_sort(nums, l, pivot)
        quick_sort(nums, pivot + 1, r)

def hoares_partition_desc(nums, l, r):
    pivot = nums[l]
    i = l
    j = r 
    while True:
        while nums[i] > pivot:
            i += 1 
        while nums[j] < pivot:
            j -= 1 
        
        if i < j:
            global desc_count
            desc_count += 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            return j 
        i += 1 
        j -= 1

def quick_sort_desc(nums, l, r):
    if l < r:
        pivot = hoares_partition_desc(nums, l, r)
        quick_sort_desc(nums, l, pivot)
        quick_sort_desc(nums, pivot + 1, r)

if __name__ == "__main__":
    # nums = [4, 6, 5, 2, 1, 3]
    nums1 = [4, 6, 7, 1, 5, 2, 3]
    nums2 = [4, 6, 7, 1, 5, 2, 3]
    quick_sort(nums1, 0, len(nums1) - 1)
    quick_sort_desc(nums2, 0, len(nums1) - 1)
    print(nums1)
    print(nums2)
    print(asc_count)
    print(desc_count)