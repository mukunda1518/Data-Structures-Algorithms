def get_two_sum(list_of_ints, two_sum):
    dict_of_ints, index = {}, 0
    for val in list_of_ints:
        if two_sum - val in dict_of_ints:
            print(dict_of_ints[two_sum - val], index)
            break
        dict_of_ints[val] = index
        index += 1 
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    # Apporach 1
    get_two_sum(nums, k)
    
    # Apporach 2
    dict_a = {}
    for i, num in enumerate(nums):
        dict_a[num] = i
    for i, num in enumerate(nums):
        diff = k - num
        if diff in dict_a:
            print(i, dict_a[diff])
            break
    
    
    
    