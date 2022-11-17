import copy

def remove_duplicates(arr):
    start = 0
    end = 0
    outer_arr = [[]]
    for i in range(len(arr)):
        start = 0
        if i > 0 and arr[i] == arr[i-1]:
            start = end
        end = len(outer_arr)
        for j in range(start, end):
            sub_arr = copy.deepcopy(outer_arr[j])
            sub_arr.append(arr[i])
            outer_arr.append(sub_arr)
    return outer_arr

if __name__ == "__main__":
    arr = [1, 2, 3]
    outer_arr = [[]]
    for num in arr:
        outer_arr_len = len(outer_arr)
        for i in range(outer_arr_len):
            sub_arr = copy.deepcopy(outer_arr[i])
            sub_arr.append(num)
            outer_arr.append(sub_arr)
    print(outer_arr)
    arr_2 = [1, 2, 2]
    print(remove_duplicates(arr_2))

