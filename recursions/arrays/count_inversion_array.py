

# Merge sort using recursion to count arr[i] > arr[j] and i < j


def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    count = 0
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            count += mid - left + 1
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]
    
    return count


def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = low + (high - low) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)
    count += merge(arr, low, mid, high)
    return count

if __name__ == "__main__":
    
    arr = [3, 1, 2, 4, 5, 2, 6, 4]
    count = merge_sort(arr, 0, len(arr) - 1)
    print(arr)
    print(count)

