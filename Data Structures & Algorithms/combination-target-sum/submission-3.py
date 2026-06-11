class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        def bt(ans, start):
            if ans and sum(ans)==target:
                self.res.append(ans.copy())
                return
            for i in range(start, len(nums)):
                if sum(ans)+nums[i]>target: break
                ans.append(nums[i])
                bt(ans, i)
                ans.pop()
        bt([], 0)
        return self.res
