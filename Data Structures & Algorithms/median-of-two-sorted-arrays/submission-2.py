class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n+m
        mid = total//2
        n1, n2 = 0,0
        count = 0
        i,j=0,0
        while i<n or j<m:
            if j>=m or (i<n and nums1[i]<nums2[j]):
                val = nums1[i]
                i+=1
            else:
                val = nums2[j]
                j+=1
            if count == mid-1:
                n1 = val
            if count == mid:
                n2 = val
                break
            count+=1
        if total%2==0: return (n1+n2)/2
        return n2