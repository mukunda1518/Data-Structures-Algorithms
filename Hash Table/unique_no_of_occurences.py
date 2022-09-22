# Leetcode: https://leetcode.com/problems/unique-number-of-occurrences/


from collections import Counter, defaultdict
def is_unique_number_of_occurences_exists(nums, n):
    # Apporach 1
    occurences = list(Counter(nums).values())    
    distinct_occurences = set(occurences)
    if len(occurences) == len(distinct_occurences):
        return True
    return False
    
    # Apporach 2
    maps1 = defaultdict(int)
    maps2 = defaultdict(int)
    for num in nums:
        maps1[num] += 1 
    for val in maps1.values():
        if maps2[val] > 0:
            return False
        maps2[val] += 1 
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(is_unique_number_of_occurences_exists(nums, n))
        
        