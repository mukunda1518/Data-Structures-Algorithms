# Leetcode: https://leetcode.com/problems/top-k-frequent-elements/
# 
# https://www.youtube.com/watch?v=YPTqKIgVk-k


from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Approach 3
        freq_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


        # Approach 1
        freq_map = Counter(nums)
        sorted_nums = sorted(freq_map.keys(), key=lambda num: freq_map[num], reverse=True)
        return sorted_nums[:k]

        # Approach 2
        min_heap = [(-c, n) for n, c in freq_map.items()]
        heapq.heapify(min_heap)
        res = []
        for _ in range(k):
            c, num = heapq.heappop(min_heap)
            res.append(num)
        return res
