
# https://www.interviewbit.com/problems/maximum-sum-combinations/

import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        m = len(B)
        A.sort(reverse=True)
        B.sort(reverse=True)
        max_heap = []
        visited = set()
        heapq.heappush(max_heap, (- (A[0] + B[0]), 0, 0))
        visited.add((0, 0))
        
        res = []
        for _ in range(C):
            if not max_heap:
                break
            curr_sum, i, j = heapq.heappop(max_heap)
            res.append(-curr_sum)
            
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(A[i+1] + B[j]), i+1, j))
                visited.add((i+1, j))
            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(A[i] + B[j + 1]), i, j + 1))
                visited.add((i, j+1))
        return res
            
