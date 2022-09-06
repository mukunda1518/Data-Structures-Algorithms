def bubble_sort(arr, r, c):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[c + 1]:
            arr[c], arr[c+1] = arr[c+1], arr[c]
        bubble_sort(arr, r, c + 1)
    else:
        bubble_sort(arr, r - 1, 0)


def selection_sort(arr, r, c, max_index):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[max_index]:
            max_index = c
        selection_sort(arr, r, c + 1, max_index)
    else:
        arr[r], arr[max_index] = arr[max_index], arr[r]
        selection_sort(arr, r - 1, 0, 0)


arr = [5, 4, 2, 1, 8, 9, 3]
bubble_sort(arr, len(arr) - 1, 0)
print(arr)

arr1 = [5, 4, 2, 1, 8, 9, 3]
selection_sort(arr1, len(arr1) - 1, 0, 0)
print(arr1)
