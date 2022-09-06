# In CustomList class we are overriding 'less than' operator with 'greater than' operator

# heapify() - O(n)
# heappush() - O(logn)
# heappop() - O(logn)
# heappushpop() - O(nlogn)
# heapreplace() - O(nlogn)




import heapq
from multiprocessing import heap

class CustomList(int):
    def __lt__(self, other):
        return self > other

a = CustomList(1)
b = CustomList(2)
c = CustomList(3)

d = 5
e = 6

arr1 = [a, b, c]
arr2 = [d, e]

heapq.heapify(arr1)
heapq.heapify(arr2)

print(arr1)
print(arr2)


class CustomList1(list):
    def __lt__(self, other):
        return self[1] < other[1]


a = CustomList1([1, 4])
b = CustomList1([2, 3])

c = [1, 4]
d = [2, 3]

arr1 = [a, b]
arr2 = [c, d]

heapq.heapify(arr1)
heapq.heapify(arr2)

print(arr1)
print(arr2)