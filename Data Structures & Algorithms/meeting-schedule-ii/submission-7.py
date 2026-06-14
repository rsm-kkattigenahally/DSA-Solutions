"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # The key idea is that when we look at start and end times in sorted order
        # while there is an end time > start time we we need to increase count because they overlap
        # The moment end time< starttime we decrease the room count as a room is free
        # we keep decreasing the room count until end times are smaller than start time
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
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
