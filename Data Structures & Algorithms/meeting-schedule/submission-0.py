"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedList = sorted(intervals, key=lambda x:x.start)
        for i in range(len(sortedList) - 1):

            if sortedList[i+1].start < sortedList[i].end:
                return False
        
        return True
