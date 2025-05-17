# https://leetcode.com/problems/longest-common-subsequence/
# https://www.youtube.com/watch?v=NPZn9jBrX8U


class Solution:

    # TC - O(2^n * 2^m)
    # SC - O(n + m)
    def get_all_lcs(self, idx1, idx2, text1, text2):
        if idx1 < 0 or idx2 < 0:
            return 0
        if text1[idx1] == text2[idx2]:
            return 1 + self.get_all_lcs(idx1 - 1, idx2 - 1, text1, text2)

        return max(self.get_all_lcs(idx1-1, idx2, text1, text2), self.get_all_lcs(idx1, idx2-1, text1, text2))

    # TC - O(2^n * 2^m)
    # SC - O(n * m) + O(n + m)
    def get_all_lcs_memo(self, idx1, idx2, text1, text2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        if text1[idx1] == text2[idx2]:
            dp[idx1][idx2] = 1 + self.get_all_lcs_memo(idx1 - 1, idx2 - 1, text1, text2, dp)
            return dp[idx1][idx2]

        dp[idx1][idx2] = max(self.get_all_lcs_memo(idx1-1, idx2, text1, text2, dp), self.get_all_lcs_memo(idx1, idx2-1, text1, text2, dp))
        return dp[idx1][idx2]
    
    # TC - O(n * m)
    # SC - O(n * m)
    def get_all_lcs_tabu(self, n, m, text1, text2):
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        # This is for base case
        # Actually the base case is for negative numbers, as it becomes complex so we are taking n as n + 1 and m as m + 1
        # so that the actually index start from 1, so we can treat 0 as negative index
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
    
    # TC - O(n * m)
    # SC - O(m)
    def get_all_lcs_tabu_space(self, n, m, text1, text2):
        # Base case
        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[m]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        return self.get_all_lcs_tabu_space(n, m, text1, text2)
        return self.get_all_lcs_tabu(n, m, text1, text2)
        dp = [[-1] * m for _ in range(n)]
        return self.get_all_lcs_memo(n-1, m-1, text1, text2, dp)

