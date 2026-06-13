"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0 or len(intervals)==1: return True
        ints = [[x.start, x.end] for x in intervals]
        ints.sort()
        i = 0
        for j in range(1, len(ints)):
            a,b = ints[i], ints[j]
            if b[0]<a[1]:
                return False
            i+=1
        return True