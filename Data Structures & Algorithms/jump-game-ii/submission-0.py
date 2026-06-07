class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        currentEnd = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i]+i)
            if currentEnd==i:
                currentEnd = farthest
                jumps+=1

        return jumps