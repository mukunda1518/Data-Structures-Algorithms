def merge(nums_with_index, start, mid, end, count):
    n1 = mid - start + 1 
    n2 = end - mid
    left_arr = [tup for tup in nums_with_index[start:mid+1]]
    right_arr = [tup for tup in nums_with_index[mid+1:end+1]]
    k = start
    i, j = 0, 0
    cnt = 0
    while k - start < n1 + n2:
        if j >= n2 or (i < n1 and left_arr[i][0] <= right_arr[j][0]):
            nums_with_index[k] = left_arr[i]
            count[left_arr[i][1]] += cnt
            i += 1
        else:
            cnt += 1
            nums_with_index[k] = right_arr[j]
            j += 1
        k += 1 
def merge_sort(nums_with_index, start, end, count):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(nums_with_index, start, mid, count)
        merge_sort(nums_with_index, mid + 1, end, count)
        # j = mid + 1
        # for i in range(start, mid + 1):
        #     while j <= end and nums_with_index[i][0] > nums_with_index[j][0]:
        #         j += 1 
        #     count[nums_with_index[i][1]] += j - (mid + 1)
        merge(nums_with_index, start, mid, end, count)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    nums_with_index = []
    for i in range(n):
        nums_with_index.append([nums[i], i])
    count = [0] * n
    merge_sort(nums_with_index, 0, n-1, count)
    print(*count)