class Solution:

    # TC - O(2^n) and more because we are taking same index multiple times
    # SC - O(n) more than this
    def min_coins_recurr(self, idx, target, coins):
        if idx == 0:
            if target % coins[idx] == 0:
                return target // coins[idx]
            else:
                return 1e9
        not_take = 0 + self.min_coins_recurr(idx - 1, target, coins)
        take = 1e9
        if coins[idx] <= target:
            take = 1 + self.min_coins_recurr(idx, target, coins)

        return min(not_take, take)
    
    # TC - O(n * target)
    # SC - O(n * target)
    def min_coins_memo(self, idx, target, coins, dp):
        if idx == 0:
            if target % coins[idx] == 0:
                return target // coins[idx]
            else:
                return 1e9
        if dp[idx][target] != -1:
            return dp[idx][target]
    
        not_take = 0 + self.min_coins_memo(idx - 1, target, coins, dp)
        take = 1e9
        if coins[idx] <= target:
            take = 1 + self.min_coins_memo(idx, target, coins, dp)

        dp[idx][target] = min(not_take, take)
        return dp[idx][target]

    # TC - O(n * target)
    # SC - O(n * target)
    def min_coins_tabu(self, coins, target):
        n = len(coins)
        if n == 1 and target % coins[0] != 0:
            return -1

        dp = [[0] * (target + 1) for _ in range(n)]

        for i in range(target + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 1e9
        
        for i in range(1, n):
            for k in range(0, target + 1):
                not_take = 0 + dp[i-1][k]
                take = 1e9
                if coins[i] <= k:
                    take = 1 + dp[i][k-coins[i]]
                dp[i][k] = min(take, not_take)
                
        print(dp)
        return -1 if dp[n-1][target] == 1e9 else dp[n-1][target]

    # TC - O(n * target)
    # SC - O(target)
    def min_coins_tabu_space(self, coins, target):
        n = len(coins)
        if n == 1 and target % coins[0] != 0:
            return -1

        prev = [0] * (target + 1)

        for i in range(target + 1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = 1e9
        
        for i in range(1, n):
            curr = [0] * (target + 1)
            for k in range(0, target + 1):
                not_take = 0 + prev[k]
                take = 1e9
                if coins[i] <= k:
                    take = 1 + curr[k-coins[i]]
                curr[k] = min(take, not_take)
            prev = curr

        return -1 if prev[target] == 1e9 else prev[target]


    def coinChange(self, coins: list[int], amount: int) -> int:
        # return self.min_coins_tabu_space(coins, amount)
        return self.min_coins_tabu(coins, amount)

s = Solution()
print(s.coinChange([1, 2, 3], 8))