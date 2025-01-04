# Quick Sort - Divide and Conqure alogorithm


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:

        while arr[i] <= pivot and i <= high:
            i += 1

        while arr[j] > pivot and j >= low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j
    

def quick_sort(arr, low, high):
    
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)

if __name__ == "__main__":
    arr = [3, 1, 2, 4, 5, 2, 6, 4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
