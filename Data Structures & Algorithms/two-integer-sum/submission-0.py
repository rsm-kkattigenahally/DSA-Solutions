class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}
        for i,n in enumerate(nums):
            if target-n in dif:
                return [dif[target-n], i]
            else:
                dif[n] = i
        