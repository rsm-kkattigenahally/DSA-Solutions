class Solution:
    def climbStairs(self, n: int) -> int:
        # Intuition: At each step i, you either came from i-1 (took 1 step) 
        # or i-2 (took 2 steps). 
        # So total ways = ways to reach i-1 + ways to reach i-2.
        if n==1 or n==2: return n
        dp = [0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

    