# Leetcode: https://leetcode.com/problems/rabbits-in-forest/

from collections import defaultdict
if __name__ == "__main__":
    n = int(input())
    answers = list(map(int, input().split()))
    map_ = defaultdict(int)
    total = 0
    for num in answers:
        if map_[num] % (num + 1) == 0:
            total += num + 1 
        map_[num] += 1
    print(total)