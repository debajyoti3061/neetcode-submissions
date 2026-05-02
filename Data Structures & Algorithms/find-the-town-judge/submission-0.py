"""
REVISION NOTES - Find The Town Judge:
• Judge trusts nobody (outgoing = 0) and everyone trusts judge (incoming = n-1)
• Track incoming and outgoing trust relationships using hashmaps
• Iterate through all people to find one with correct trust pattern
• Judge must have exactly n-1 incoming trusts and 0 outgoing trusts
• Time: O(E + N), Space: O(N) where E is edges, N is people
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1
        for i in range(1,n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1
        