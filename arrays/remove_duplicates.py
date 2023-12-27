from sortedcontainers import SortedSet

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]

    # Brute Force Solution - O(nlogn * n)
    # sorted_set = SortedSet()
    # for ele in arr:
    #     sorted_set.add(ele)
    # len_ = len(sorted_set)
    
    # for i in range(len_):
    #     arr[i] = sorted_set[i]
    # print(arr)

# optimised approach - O(n)

    f_pointer = 0
    for s_pointer in range(1, len(arr)):
        if arr[f_pointer] != arr[s_pointer]:
            f_pointer += 1
            arr[f_pointer] = arr[s_pointer]
    print(arr)
    
    