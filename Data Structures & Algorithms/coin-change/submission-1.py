class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # the key idea is that here we need to check the min num of coins req to make amount 1...n with given coins
        dp = [float("inf")]*(amount+1)
        dp[0] = 0 # since we need 0 coins to make 0 units on money
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i], 1+dp[i-c])
        if dp[-1]==float("inf"): return -1
        return dp[-1]
