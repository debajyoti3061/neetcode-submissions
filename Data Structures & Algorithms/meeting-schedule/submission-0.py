"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
REVISION NOTES - Meeting Schedule:
• Sort intervals by start time to process them chronologically
• Check each consecutive pair of intervals for overlap
• If previous meeting ends after current meeting starts, there's conflict
• Return False if any overlap found, True if all meetings can be attended
• Sorting ensures we only need to check adjacent intervals
• Time: O(n log n), Space: O(1)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        for i in range (1,len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        
        return True
