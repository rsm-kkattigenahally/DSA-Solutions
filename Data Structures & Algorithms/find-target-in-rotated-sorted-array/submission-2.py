class Solution:
    def search(self, nums: List[int], target: int) -> int:
        small = float("inf")
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            if nums[mid]>=nums[l]: # left is sorted check inclusive of mid 
                if nums[l]<= target< nums[mid]:  # check inclusive of left value
                    r = mid-1
                else:
                    l = mid+1
            else : # right is sorted
                if nums[mid]< target<= nums[r]:   # check inclusive of right value
                    l = mid+1
                else:
                    r = mid-1
        return -1

