"""
REVISION NOTES - Insert New Interval:
• Iterate through existing intervals and handle 3 cases:
• Case 1: newInterval ends before current interval starts → insert newInterval and return
• Case 2: newInterval starts after current interval ends → add current interval to result
• Case 3: Intervals overlap → merge by updating newInterval bounds
• After loop, append final newInterval (handles case where it goes at the end)
• Time: O(n), Space: O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res
        