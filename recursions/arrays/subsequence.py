# Print all subsequences of an array

# Time Complexity - O(2^^n)
# Space Complexity - O(n)

def print_subsequnces(indx, n, subseq, arr):
    if indx == n:
        print(subseq)
        return
    
    subseq.append(arr[indx])
    print_subsequnces(indx + 1, n, subseq, arr)
    subseq.pop()
    print_subsequnces(indx + 1, n, subseq, arr)


if __name__ == "__main__":
    arr = [3, 2, 1]
    print_subsequnces(0, len(arr), [], arr)
    
