
from array import array


def build_max_heap(arr):
    for i in range(len(arr) // 2, 0, -1):
        max_heapify(arr, i)

def extract_max(array):
    n = len(array)
    if n < 1:
        return
    max_ = array[1]
    array[1] = array[n]
    n = n - 1 
    max_heapify(array, 1)
    return max_


def max_heapify(arr, i):
    left = 2 * i 
    right = 2 * i + 1 

    if left <= len(arr) and arr[left] > arr[i]:
        largest = left 
    else:
        largest = i 
    
    if right <= len(arr) and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)

def bottom_up_heapify(array, heap_size):
    i = heap_size
    while i > 1 and array[i//2] < array[i]:
        array[i], array[i//2] = array[i], array[i//2]
        i = i // 2
        
def insert(array, x):
    heap_size = len(array)
    heap_size = heap_size + 1 
    array[heap_size] = x 
    bottom_up_heapify(array, heap_size)