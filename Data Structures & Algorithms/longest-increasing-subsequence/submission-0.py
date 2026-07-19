class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            tmp = dp[i]
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], tmp+dp[j])
        return max(dp)
