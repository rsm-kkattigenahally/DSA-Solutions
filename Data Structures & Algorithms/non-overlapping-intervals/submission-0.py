class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # The key idea is sort the intervals by end time
        # [[1,2],[2,4],[1,4]] -- [1,2][2,4][1,4]
        # we do this bcz we  want to check for overlaps on the earliest intervals
        # set prev = intervals[0][1]
        # check if prev>curr int[0] then there is an overlap and we remove.
        # You always keep the one with the earlier end time and remove the other.
        #  keeping the interval that ends earliest leaves maximum room for future intervals.
        # else we set prev = curr int
        intervals.sort(key = lambda x:x[1])
        prev = intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if prev>intervals[i][0]:   # overlap
                count+=1
            else:
                prev = intervals[i][1]
        return count


                

