class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        a = 1
        water = 0
        while i<j:
            a = abs(i-j)*min(heights[i], heights[j])
            water = max(water, a)
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return water