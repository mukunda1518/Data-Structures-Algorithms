# Count all sub sequences with sum k  -------- i.e 2 in this case

# Time Complexity - O(2^^n)
# Space Complexity - O(n)

def check_subsequence(idx, n, sub_seq, e_sum, arr, a_sum):
    if idx == n:
        if e_sum == a_sum:
            print(sub_seq)
            return 1
        return 0
    sub_seq.append(arr[idx])
    e_sum += arr[idx]
    l_count = check_subsequence(idx + 1, n, sub_seq, e_sum, arr, a_sum)
    sub_seq.pop()
    e_sum -= arr[idx]
    r_count = check_subsequence(idx + 1, n, sub_seq, e_sum, arr, a_sum)
    return  l_count + r_count


if __name__ == "__main__":
    arr = [1, 2, 1, 5]
    print(f"No of sub sequence with sum 2: {check_subsequence(0, len(arr), [], 0, arr, 2)}")

