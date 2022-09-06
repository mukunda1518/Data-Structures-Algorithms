#  count of num is > len(nums) // 3


def get_number_more_than_n_third(nums, n):
    k = n // 3
    num_count_dict = {}
    for num in nums:
        if not num_count_dict.get(num, 0):
            num_count_dict[num] = 1 
        else:
            num_count_dict[num] += 1 
    flag = False
    for key, val in num_count_dict.items():
        if val > k:
            print(key)
            flag = True
            break
    if not flag:
        print("NONE")
        


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    # get_number_more_than_n_third(nums, n)
    count1 = count2 = first = second = 0
    for i in range(n):
        if first == nums[i]:
            count1 += 1 
        elif second == nums[i]:
            count2 += 1 
        elif count1 == 0:
            count1 += 1 
            first = nums[i]
        elif count2 == 0:
            count2 += 1 
            second = nums[i]
        else:
            count1 -= 1 
            count2 -= 1 
    count1 = count2 = 0
    
    for i in range(n):
        if nums[i] == first:
            count1 += 1 
        elif nums[i] == second:
            count2 += 1 
    
    if count1 > n // 3:
        print(first)
    elif count2 > n // 3:
        print(second)
    else:
        print("NONE")
    
    
        