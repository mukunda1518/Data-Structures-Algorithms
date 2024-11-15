
# Leetcode - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 
 # Time Complexity - O(n^2)

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        max_score = 0
        for i in range(k):
            max_score = max(max_score, sum(cardPoints[0:i]) + sum(cardPoints[i-k:]))
        max_score = max(max_score, sum(cardPoints[0:k]))
        return max_score


# Time Complexity - O(n)

class Solution1:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        start_sum = 0
        end_sum = sum(cardPoints[-k:])
        max_score = end_sum
        for i in range(k):
            max_score = max(max_score, start_sum + end_sum)
            start_sum += cardPoints[i]
            end_sum -= cardPoints[n - k + i]
        max_score = max(max_score, start_sum)
        return max_score

if __name__ == "__main__":
    card_points = list(map(int, input().split(",")))
    k = int(input())
    print(Solution().maxScore(card_points, k))
    print(Solution1().maxScore(card_points, k))
    