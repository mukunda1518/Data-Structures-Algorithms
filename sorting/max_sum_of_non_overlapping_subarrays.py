def get_sum_of_left_sub_arrays(nums, n, l):
    left_array = [0] * n
    sum_ = sum(nums[0:l])
    left_array[l - 1] = sum_
    s, max_ = 0, sum_

    for e in range(l, n):
        sum_ += nums[e] - nums[s]
        max_ = max(max_, sum_)
        left_array[e] = max_
        s += 1
    return left_array


def get_sum_of_right_sub_arrays(nums, n, m):
    right_array = [0] * n
    sum_ = sum(nums[n - m:n])
    right_array[n - m] = sum_
    s, max_ = n - 1, sum_
    for e in range(n - m - 1, -1, -1):
        sum_ += nums[e] - nums[s]
        max_ = max(max_, sum_)
        right_array[e] = max_
        s -= 1
    return right_array


def get_max_sum(left_array, right_array, k):
    max_sum = 0
    for i in range(k - 1, len(left_array) - 1):
        max_sum = max(max_sum, left_array[i] + right_array[i + 1])
    return max_sum


# Don't work
# def get_max_sum1(nums, l, m):
#     l_sum = l_max = sum(nums[0:l])
#     r_sum = r_max = sum(nums[l:l+m])
#     l_s, l_e = 0, l
#     r_s, r_e = l, l+m
#     while r_e < len(nums):
#         l_sum += nums[l_e] - nums[l_s]
#         r_sum += nums[r_e] - nums[r_s]
#         l_max = max(l_sum, l_max)
#         r_max = max(r_sum, r_max)
#         l_s += 1
#         l_e += 1
#         r_s += 1
#         r_e += 1
#     return l_max + r_max


def max_sum(nums, l, m):
    for i in range(1, n):
        nums[i] += nums[i - 1]

    res = nums[l + m - 1]
    l_max = nums[l - 1]
    m_max = nums[m - 1]

    for i in range(l + m, len(nums)):
        l_max = max(l_max, nums[i - m] - nums[i - m - l])
        res_1 = l_max + nums[i] - nums[i - m]
        m_max = max(m_max, nums[i - l] - nums[i - l - m])
        res_2 = m_max + nums[i] - nums[i - l]
        res = max(res, res_1, res_2)
    return res


if __name__ == "__main__":
    n, l, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(max_sum(nums, l, m))

    # # with l, m sizes
    # left_array = get_sum_of_left_sub_arrays(nums, n, l)
    # right_array = get_sum_of_right_sub_arrays(nums, n, m)
    # max_sum_1 = get_max_sum(left_array, right_array, l)

    # # with m, l sizes
    # left_array = get_sum_of_left_sub_arrays(nums, n, m)
    # right_array = get_sum_of_right_sub_arrays(nums, n, l)
    # max_sum_2 = get_max_sum(left_array, right_array, m)

    # print(max(max_sum_1, max_sum_2))
