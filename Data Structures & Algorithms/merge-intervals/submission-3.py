class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # a = [1,3] b = [1,5]
        # a[0]<=b[0] and a[1]>=b[0]
        # new = [min(a[0], b[0]), max(a[1], b[1])]
        if len(intervals)==1: return intervals
        i = 1
        intervals.sort()
        ints = []
        newinter = intervals[0]
        while i<len(intervals):
            inter = intervals[i]
            if newinter[1]<inter[0]:
                ints.append(newinter)
                i+=1
                newinter = inter
            else:
                newinter = [min(newinter[0], inter[0]), max(newinter[1], inter[1])]
                i+=1
        ints.append(newinter)
        return ints
