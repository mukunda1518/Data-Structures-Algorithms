# Leetcode Question: https://leetcode.com/contest/weekly-contest-310/problems/most-frequent-even-element/

from collections import Counter

class Solution:

    def mostFrequentEven(self, nums) -> int:
        nums_freq = list(Counter(nums).items())
        nums_freq = sorted(nums_freq, key= lambda pair:(-pair[1], pair[0]))
        freq_even_num = -1
        freq_count = 0
        for key, val in nums_freq:
            if key % 2 == 0 and freq_count < val:
                freq_even_num = key
                freq_count = val
        return freq_even_num