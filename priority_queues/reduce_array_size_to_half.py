# Leetcode: https://leetcode.com/problems/reduce-array-size-to-the-half/


from collections import Counter
# For most_common() functionality: https://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_dict = Counter(arr)
        # tuples = list(arr_dict.items())
        # tuples = sorted(tuples, key=lambda pair: (pair[1], pair[0]), reverse=True)
        half_len = len(arr) // 2
        tuples = arr_dict.most_common(half_len)
        total = 0
        count = 0
        for key, val in tuples:
            total += val
            count += 1
            if total >= half_len:
                return count