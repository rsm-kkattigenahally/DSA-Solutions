class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = -float("inf")
        currsub = -float("inf")
        for i in range(len(nums)):
            currsub = max(currsub+nums[i], nums[i])
            maxsub = max(maxsub, currsub)
        return maxsub