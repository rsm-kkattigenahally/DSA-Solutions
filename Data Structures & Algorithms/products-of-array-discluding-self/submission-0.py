class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 1 , 1]
        # prefix = [1, 1, 2, 8]
        # [ 48, 24 ,12 ,8]

        prefix = [1]*len(nums)
        n = len(nums)
       
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix = [1]*n
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        print(prefix, suffix)
        for i in range(n):
            suffix[i] = suffix[i]*prefix[i]
        
        return suffix
