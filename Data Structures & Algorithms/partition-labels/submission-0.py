"""
REVISION NOTES - Partition Labels:
• Greedy approach: find last occurrence of each character first
• Track the farthest position needed to include all characters seen so far
• When current position equals the farthest position, we can make a partition
• Each partition contains all occurrences of its characters
• Record size of each partition as we complete them
• Time: O(n), Space: O(1) - at most 26 characters
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0

        for i,c in enumerate(s):
            size += 1
            end = max(end,lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res
        