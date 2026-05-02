"""
REVISION NOTES - Merge Intervals:
- Sort intervals by start time
- Merge overlapping intervals by comparing end times
- If current start <= previous end, merge by updating end time
- Otherwise, add current interval to result
- Time: O(n log n), Space: O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]
        for start,end in intervals:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output


        