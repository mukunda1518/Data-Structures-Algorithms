# list_a = []
#
# def found_element(arr, target, index):
#     if index == len(arr):
#         return
#     if arr[index] == target:
#         list_a.append(index)
#     found_element(arr, target, index + 1)
#     # return arr[index] == target || found_element(arr, target, index + 1)
#
# if __name__ == "__main__":
#     arr = [5, 8, 1, 2, 3, 5, 6, 7, 5]
#     target = 5
#     found_element(arr, target, 0)
#     print(list_a)


# def found_element_indexs(arr, target, index, list_a):
#     if index == len(arr):
#         return list_a
#     if arr[index] == target:
#         list_a.append(index)
#     return found_element_indexs(arr, target, index + 1, list_a)

#
# if __name__ == "__main__":
#     arr = [5, 8, 1, 2, 3, 5, 6, 7, 5]
#     target = 5
#     list_a = []
#     print(found_element_indexs(arr, target, 0, list_a))


def found_element_indexs(arr, target, index):
    list_a = []
    if index == len(arr):
        return list_a
    if arr[index] == target:
        list_a.append(index)
    list_from_below_calls = found_element_indexs(arr, target, index + 1)
    return list_from_below_calls.extend(list_a)
    # return list_a + found_element_indexs(arr, target, index + 1)

if __name__ == "__main__":
    arr = [5, 8, 1, 2, 3, 5, 6, 7, 5]
    target = 5
    list_a = []
    print(found_element_indexs(arr, target, 0))
