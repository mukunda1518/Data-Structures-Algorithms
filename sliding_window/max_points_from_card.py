# Leetcode: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        start_sum = 0
        end_sum = sum(cardPoints[-k:])
        max_score = end_sum
        for i in range(k):
            start_sum += cardPoints[i]
            end_sum -= cardPoints[n - k + i]
            max_score = max(max_score, start_sum + end_sum)
        return max_score
