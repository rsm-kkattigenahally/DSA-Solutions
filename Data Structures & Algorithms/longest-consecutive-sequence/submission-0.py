class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        count = 0
        max_count = 0
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            while curr+1 in n:
                count+=1
                curr = curr+1
            max_count = max(max_count, count)
        return max_count
