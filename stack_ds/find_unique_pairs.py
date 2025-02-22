from collections import deque
# -- Brute Froce Apporach
def get_max_and_sec_max(sub_arr):
    len_ = len(sub_arr)
    x = max(sub_arr)
    y = min(sub_arr)
    for num in sub_arr:
        if num < x and num > y:
            y = num
    return (x, y)

def get_unique_pairs_count(nums, n):
    unique_pairs = []
    for k in range(2, n+1):
        for j in range(0, n - k + 1):
            sub_arr = nums[j:k+j]
            x, y = get_max_and_sec_max(sub_arr)
            if (x, y) not in unique_pairs:
                unique_pairs.append((x, y))
    return len(unique_pairs)

# Time Complexity : O(n)
def count_pairs(nums, n):
    forward = [0 for _ in range(n)]
    sforward = deque([])
    for i in range(n):
        while sforward and nums[i] > nums[sforward[-1]]:
            forward[sforward[-1]] = 1 
            sforward.pop()
        sforward.append(i)
    
    backward = [0 for _ in range(n)]
    sbackward = deque([])
    for i in reversed(range(n)):
        while sbackward and nums[i] > nums[sbackward[-1]]:
            backward[sbackward[-1]] = 1 
            sbackward.pop()
        sbackward.append(i)
    
    count = 0
    for i in range(n):
        count += forward[i] + backward[i]
    return count

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(count_pairs(nums, n))
    # print(get_unique_pairs_count(nums, n))