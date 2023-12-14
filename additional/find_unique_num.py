# Time complexity - O(n)


def find_unique_num(arr):
    u_num = 0
    for i in arr:
        u_num = u_num ^ i
    print(u_num)



if __name__ == "__main__":
    arr = [2, 3, 5, 4, 1, 1, 5, 3, 2, 6, 4]
    find_unique_num(arr)