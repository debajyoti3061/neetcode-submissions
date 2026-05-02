"""
REVISION NOTES - Non-Overlapping Intervals:
• Greedy approach: sort intervals by start time
• Track end time of last kept interval
• If current interval doesn't overlap, keep it and update end time
• If overlap occurs, remove interval with later end time (keep earlier ending one)
• Count number of intervals removed to make all non-overlapping
• Time: O(n log n), Space: O(1)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd= end
            else:
                res += 1
                prevEnd = min(end,prevEnd)
        return res
        