
def get_no_of_ways(r, c):
    if r == 1 or c == 1:
        return 1
    left = get_no_of_ways(r - 1, c)
    right = get_no_of_ways(r, c-1)
    return left + right


def get_paths(p_path, r, c):
    if r == 1 and c == 1:
        print(p_path)
        return
    if r > 1:
        get_paths(p_path + "D", r - 1, c)
    if c > 1:
        get_paths(p_path + "R", r, c - 1)


def get_paths_list(p_path, r, c):
    if r == 1 and c == 1:
        return [p_path]
    res = []
    if r > 1:
        res.extend(get_paths_list(p_path + "D", r - 1, c))
    if c > 1:
        res.extend(get_paths_list(p_path + "R", r, c - 1))
    return res


def get_paths_along_with_diagonally(p_path, r, c):
    if r == 1 and c == 1:
        return [p_path]
    res = []
    if r > 1 and c > 1:
        res.extend(get_paths_along_with_diagonally(p_path + "D", r - 1, c - 1))
    if r > 1:
        res.extend(get_paths_along_with_diagonally(p_path + "V", r - 1, c))
    if c > 1:
        res.extend(get_paths_along_with_diagonally(p_path + "H", r, c - 1))
    return res


def get_paths_obstacles(p_path, arr, r, c):
    if r == len(arr) - 1 and c == len(arr[0]) - 1:
        return [p_path]
    if arr[r][c]:
        return []
    res = []
    if r < len(arr) - 1:
        res.extend(get_paths_obstacles(p_path + "D", arr, r + 1, c))
    if c < len(arr[0]) - 1:
        res.extend(get_paths_obstacles(p_path + "R", arr, r, c + 1))
    return res


if __name__ == "__main__":
    print(get_no_of_ways(3, 3))
    get_paths("", 3, 3)
    print(get_paths_list("", 3, 3))
    print(get_paths_along_with_diagonally("", 3, 3))
    arr = [
        [False, False, False],
        [False, True, False],
        [False, False, False]
    ]
    print(get_paths_obstacles("", arr, 0, 0))