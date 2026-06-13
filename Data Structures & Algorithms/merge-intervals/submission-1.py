class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # a = [1,3] b = [1,5]
        # a[0]<=b[0] and a[1]>=b[0]
        # new = [min(a[0], b[0]), max(a[1], b[1])]
        if len(intervals)==1: return intervals
        n =len(intervals)
        intervals.sort()
        ints = []
        newInt = intervals[0]
        i = 1
        while i<n:
            inter = intervals[i]
            if newInt[1]<inter[0]:
                ints.append(newInt)
                newInt = inter
                i+=1
            else:
                newInt = [min(inter[0], newInt[0]), max(inter[1], newInt[1])]
                i+=1
        ints.append(newInt)
        return ints
