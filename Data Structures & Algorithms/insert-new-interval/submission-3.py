class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Identify 3 phases
        # Before the new interval, overlapping, after the new int
        i = 0
        ints = []
        while i<len(intervals) and intervals[i][1]< newInterval[0]:
            ints.append(intervals[i])
            i+=1
        st, end = None, None
        while i<len(intervals) and intervals[i][0]<=newInterval[1] :
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        ints.append(newInterval)

        if i<len(intervals):
            ints = ints+intervals[i:]
        return ints
        