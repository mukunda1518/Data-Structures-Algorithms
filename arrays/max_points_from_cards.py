# Leetcode: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s_sum = 0
        e_sum = 0
        n = len(cardPoints)
        for i in range(n-1, n - k - 1, -1):
            e_sum += cardPoints[i]
        j = n - k
        max_sum = e_sum
        for i in range(0, k):
            s_sum += cardPoints[i]
            e_sum -= cardPoints[j]
            max_sum = max(max_sum, s_sum + e_sum)
            j += 1
        return max_sum