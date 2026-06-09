class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s==0: 
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif s>0:
                    k-=1
                else:
                    j+=1
                
        reslist = [list(x) for x in res]
        return reslist


            