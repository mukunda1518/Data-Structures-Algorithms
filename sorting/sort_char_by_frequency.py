# Leetcode: https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([key * val for key, val in Counter(s).most_common()])
        # Approach - 2
        s_freq = list(Counter(s).items())
        s_freq.sort(key=lambda pair: (-pair[1], pair[0]))
        s1 = ""
        for tup in s_freq:
            s1 += tup[0] * tup[1]
        return s1
        
        