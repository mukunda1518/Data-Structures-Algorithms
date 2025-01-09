
# Print all Permutations of a String/Array | Recursion | Approach - 2
# https://www.youtube.com/watch?v=f2ic2Rsc9pU&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=15


# Time Complexity - O(n!) * O(n)

def get_all_permutations(idx, n, arr, res):
    if idx >= n:
        res.append(arr.copy())
        return

    for i in range(idx, n):
        arr[i], arr[idx] = arr[idx], arr[i]
        get_all_permutations(idx + 1, n, arr, res)
        arr[i], arr[idx] = arr[idx], arr[i]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    res = []

    get_all_permutations(0, n, arr, res)
    print(res)
