


class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return (index * 2) + 1

    def _right_child(self, index):
        return (index * 2) + 2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        # Ensures the heap property is maintained from bottom to top
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            self.index = self._parent(index)

    def pop(self):
        if self.size == 0:
            return "No elements in heap"
        self._swap(0, self.size - 1)
        value = self.heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return value

    def heapify_down(self, index):
        # Ensures the heap property is maintained from top to bottom
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self.heapify_down(smallest)

    def heapify(self, arr): # O(n)
        self.heap = arr[:]
        self.size = len(arr)
        for i in range(self._parent(self.size - 1), -1, -1):
            self.heapify_down(i)

    def heap_sort(self, arr): # O(n) + O(nlogn) = O(nlogn)
        self.heapify(arr)
        sorted_list = []
        while self.heap:
            sorted_list.append(self.pop())
        return sorted_list

    def peek(self):
        if self.size == 0:
            return "No elements in heap"
        return self.heap[0]

    def is_empty(self):
        return self.size == 0

if __name__ == "__main__":
    heap = MinHeap()
    arr = [5, 3, 8, 1, 2, 7]
    print("Original array:", arr)
    sorted_arr = heap.heap_sort(arr)
    print("Sorted array:", sorted_arr)