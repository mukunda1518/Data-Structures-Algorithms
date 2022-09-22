# Leetcode : https://leetcode.ca/2016-08-22-266-Palindrome-Permutation/

from collections import defaultdict

def check_is_permutation_palindrome(string):
    set_ = set()
    for char in string:
        if char in set_:
            set_.remove(char)
        else:
            set_.add(char)
    if len(set_) <= 1:
        return "YES"
    else:
        return "NO"

def is_permute_palindrome(s):
    max_odd_count = 0 if len(s) % 2 == 0 else 1
    map_ = defaultdict(int)
    for i in range(len(s)):
        map_[s[i]] += 1 
    
    odd_count = 0
    for key in map_:
        if map_[key] % 2 == 1:
            odd_count += 1 
        if odd_count > max_odd_count:
            return "NO"
    return "YES"
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        string = input()
        print(check_is_permutation_palindrome(string))