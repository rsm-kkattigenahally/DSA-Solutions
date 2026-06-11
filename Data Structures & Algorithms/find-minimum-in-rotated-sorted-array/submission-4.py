class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums)==1: return nums[0]
        small = None
        while l<=r:
            mid = (l+r)//2
            if small is None: small = nums[mid]
            if nums[mid]<small: small = nums[mid]
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid-1

            
        return small


               