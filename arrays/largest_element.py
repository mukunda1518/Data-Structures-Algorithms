import sys


# Time Complexity for sorting method - O(nlogn) | Space Complexity - O(1)
# Time Complexity - O(n) | Space Complexity - O(1)

if __name__ == "__main__":
    arr = [3, 1, 2, 5, 2]
    print(sorted(arr)[-1])
    max_ = float("-inf")
    sec_max = float("-inf")
    for ele in arr:
        if ele > max_:
            sec_max = max_
            max_ = ele
        elif ele > sec_max and ele != max_:
            sec_max = ele
    print(max_, sec_max)


