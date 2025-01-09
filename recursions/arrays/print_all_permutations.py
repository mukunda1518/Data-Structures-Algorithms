
# Print all Permutations of a String/Array | Recursion | Approach - 1
# https://www.youtube.com/watch?v=YK78FU5Ffjw&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=14


# Time Complexity - O(n!) * O(n)
# Space Complexity - O(n)

def get_all_permutations(ds, n, mp, arr, res):
    if len(ds) == n:
        res.append(ds.copy())
        return

    for i in range(n):
        if not mp.get(i):
            ds.append(arr[i])
            mp[i] = 1
            get_all_permutations(ds, n, mp, arr, res)
            mp[i] = 0
            ds.pop()


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    res = []
    mp = {}

    get_all_permutations([], n, {}, arr, res)
    print(res)
