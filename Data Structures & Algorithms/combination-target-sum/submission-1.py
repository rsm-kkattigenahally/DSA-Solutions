class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.resset=set()
        def bt(ans):
            if ans and sum(ans)>target: return
            if ans and sum(ans)==target :
                if tuple(sorted(ans)) not in self.resset:
                    self.res.append(sorted(ans))
                    self.resset.add(tuple(sorted(ans)))
                    return 
                else:
                    return

            for i in range(len(nums)):
                ans.append(nums[i])
                bt(ans)
                ans.pop()
        bt([])
        return self.res