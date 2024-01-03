class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False





from collections import defaultdict

class Solution1:

    def _get_upper_bound(self, arr, target):
        left, right = 0, len(arr) - 1
        flag = False
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > target:
                flag = True
                right -= 1
            else:
                left += 1
        return flag, arr[mid]

    def isSubsequence(self, s: str, t: str) -> bool:
        # if not s:
        #     return True
        # j = 0
        # for i in range(len(t)):
        #     if t[i] == s[j]:
        #         j += 1
        #     if j == len(s):
        #         return True
        # return False
    
        t_char_map = defaultdict(list)
        for i, char in enumerate(t):
            t_char_map[char].append(i)
        
        prev = -1
        for char in s:
            if char in t_char_map:
                is_found, indx = self._get_upper_bound(t_char_map[char], prev)
                if is_found:
                    prev = indx
                else:
                    return False
            else:
                return False
        return True
        