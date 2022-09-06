
def get_all_paths(p_path, arr, r, c):
    if r == len(arr) - 1 and c == len(arr[0]) - 1:
        print(p_path)
        return
    if arr[r][c]:
        return
    arr[r][c] = True
    res = []
    if r < len(arr) - 1:
        get_all_paths(p_path + "D", arr, r + 1, c)
    if c < len(arr[0]) - 1:
        get_all_paths(p_path + "R", arr, r, c + 1)
    if r > 0:
        get_all_paths(p_path + "U", arr, r - 1, c)
    if c > 0:
        get_all_paths(p_path + "L", arr, r, c - 1)

    # This is line is where the function will be over
    # So before the function gets removed also remove the changes that were made by the function
    arr[r][c] = False


def get_all_paths_list(p_path, arr, r, c):
    if r == len(arr) - 1 and c == len(arr[0]) - 1:
        return [p_path]
    if arr[r][c]:
        return []
    arr[r][c] = True
    res = []
    if r < len(arr) - 1:
        res.extend(get_all_paths_list(p_path + "D", arr, r + 1, c))
    if c < len(arr[0]) - 1:
        res.extend(get_all_paths_list(p_path + "R", arr, r, c + 1))
    if r > 0:
        res.extend(get_all_paths_list(p_path + "U", arr, r - 1, c))
    if c > 0:
        res.extend(get_all_paths_list(p_path + "L", arr, r, c - 1))

    # This is line is where the function will be over
    # So before the function gets removed also remove the changes that were made by the function
    arr[r][c] = False
    return res


def get_all_paths_and_steps(p_path, arr, r, c, path_arr, steps):
    if r == len(arr) - 1 and c == len(arr[0]) - 1:
        path_arr[r][c] = steps
        for a in path_arr:
            print(a.copy())
        print(p_path)
        print()
        return
    if arr[r][c]:
        return
    arr[r][c] = True
    path_arr[r][c] = steps
    if r < len(arr) - 1:
        get_all_paths_and_steps(p_path + "D", arr, r + 1, c, path_arr, steps + 1)
    if c < len(arr[0]) - 1:
        get_all_paths_and_steps(p_path + "R", arr, r, c + 1, path_arr, steps + 1)
    if r > 0:
        get_all_paths_and_steps(p_path + "U", arr, r - 1, c, path_arr, steps + 1)
    if c > 0:
        get_all_paths_and_steps(p_path + "L", arr, r, c - 1, path_arr, steps + 1)

    # This is line is where the function will be over
    # So before the function gets removed also remove the changes that were made by the function
    arr[r][c] = False
    path_arr[r][c] = 0


if __name__ == "__main__":
    arr = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]
    get_all_paths("", arr, 0, 0)
    print(get_all_paths_list("", arr, 0, 0))
    path_arr = [[0] * 3, [0] * 3, [0] * 3]
    get_all_paths_and_steps("", arr, 0, 0, path_arr, 1)

