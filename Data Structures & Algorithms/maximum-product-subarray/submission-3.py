class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod, maxprod = 1,1
        res = -float("inf")
        for n in nums:
            tmp = maxprod*n
            maxprod = max(tmp, minprod*n, n)
            minprod = min(tmp, minprod*n, n)
            res = max(res, maxprod)
         
        return res
