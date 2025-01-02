
# Print all sub sequences with sum k i.e 2 in this case

# Time Complexity - O(2^^n)
# Space Complexity - O(n)

def print_sub_seq_with_sum_k(idx, n, sub_seq, e_sum, arr, a_sum):
    if idx == n:
        if e_sum == a_sum:
            print(sub_seq)
        return
    sub_seq.append(arr[idx])
    e_sum += arr[idx]
    print_sub_seq_with_sum_k(idx + 1, n, sub_seq, e_sum, arr, a_sum)
    sub_seq.pop()
    e_sum -= arr[idx]
    print_sub_seq_with_sum_k(idx + 1, n, sub_seq, e_sum, arr, a_sum)


if __name__ == "__main__":
    arr = [1, 2, 1, 5]
    print_sub_seq_with_sum_k(0, len(arr), [], 0, arr, 2)
    
