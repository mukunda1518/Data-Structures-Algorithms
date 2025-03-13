# Leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/


import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]




# ---------------------------------------------------------------------------



# Using quick select



class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def partition_index(l, h):
            pivot = nums[l]
            i, j = l, h

            while i < j:

                while i <= h and nums[i] <= pivot:
                    i += 1
                
                while j >= l and nums[j] > pivot:
                    j -= 1
                
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[l], nums[j] = nums[j], nums[l]
            return j

        def quick_select(l, h):
            if l == h:
                return nums[l]
            if l < h:
                p_index = partition_index(l, h)            
                if k < p_index:
                    return quick_select(l, p_index - 1)
                elif k > p_index:
                    return quick_select(p_index + 1, h)
                else:
                    return nums[p_index]

        return quick_select(0, len(nums) - 1)
