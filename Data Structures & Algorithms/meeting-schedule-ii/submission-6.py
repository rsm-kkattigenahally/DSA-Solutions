"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        print(starts, ends)
        count = 0
        i = 0
        maxcount = 0
        for j in range(len(starts)):
            while i<len(ends) and ends[i]<=starts[j]:
                count-=1
                i+=1
            count+=1
            maxcount = max(maxcount, count)
        return maxcount
