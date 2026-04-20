"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key = lambda i : i.start)

        res = []
        res.append(intervals[0].end)
        heapq.heapify(res)
        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = res[0]
            if start >= end:
                heapq.heappop(res)
            heapq.heappush(res,intervals[i].end)
        
        return len(res)
        