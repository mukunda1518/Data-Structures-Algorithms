
def search(arr, target, l, r):
    if l > r:
        return -1
    mid = l + (r - l) // 2

    if arr[mid] == target:
        return mid

    if arr[l] <= arr[mid]:
        if target >= arr[l] and target <= arr[mid]:
            return search(arr, target, l, mid - 1)
        else:
            return search(arr, target, mid+1, r)
    if target >= arr[mid] and target <= arr[r]:
        return search(arr, target, mid + 1, r)
    else:
        return search(arr, target, l, mid - 1)

if __name__ == "__main__":
    arr = [10, 11, 12, 13, 1, 2, 3, 4, 5]
    target = 15
    print(search(arr, target, 0, len(arr) - 1))
