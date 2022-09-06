def isarrysorted(arr, index):
    if index == len(arr) - 1:
        return True

    return arr[index] < arr[index + 1] and isarrysorted(arr, index + 1)

if __name__ == "__main__":
    arr = [8, 1, 2, 3, 5, 6, 7]
    print(isarrysorted(arr, 0)) 