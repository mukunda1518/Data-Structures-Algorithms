def get_array_combinations(comb, no_of_array):
    if not len(no_of_array):
        return [comb]
    res_arr = []
    arr = no_of_array[0]
    for num in arr:
        res_arr.extend(get_array_combinations(comb + str(num), no_of_array[1:]))
    return res_arr


if __name__ == "__main__":
    no_of_arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(get_array_combinations("", no_of_arr))
