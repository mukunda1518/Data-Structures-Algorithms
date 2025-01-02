# Check does sub sequences with sum k esists ---- i.e 2 in this case
# Return true if atleast one subsequence exists


# Time Complexity - O(2^^n)
# Space Complexity - O(n)

def check_subsequence(idx, n, sub_seq, e_sum, arr, a_sum):
    if idx == n:
        if e_sum == a_sum:
            print(sub_seq)
            return True
        return False
    sub_seq.append(arr[idx])
    e_sum += arr[idx]
    if check_subsequence(idx + 1, n, sub_seq, e_sum, arr, a_sum):
        return True
    sub_seq.pop()
    e_sum -= arr[idx]
    if check_subsequence(idx + 1, n, sub_seq, e_sum, arr, a_sum):
        return True
    return False


if __name__ == "__main__":
    arr = [1, 2, 1, 5]
    check_subsequence(0, len(arr), [], 0, arr, 2)
    
