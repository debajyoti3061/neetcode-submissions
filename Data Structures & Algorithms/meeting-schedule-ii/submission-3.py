"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
REVISION NOTES - Meeting Schedule II:
• Sort intervals by start time, use min-heap to track room end times
• For each meeting, check if earliest ending room is available
• If current meeting starts after earliest room ends, reuse that room
• Otherwise, need a new room - add current meeting's end time to heap
• Heap size represents minimum number of rooms needed
• Time: O(n log n), Space: O(n)
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
        