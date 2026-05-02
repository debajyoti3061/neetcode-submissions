"""
REVISION NOTES - Car Fleet:
- Sort cars by position (descending order)
- Calculate time to reach target for each car
- Use stack to track fleet formation
- Cars with longer time will form separate fleets
- Time: O(n log n), Space: O(n)
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p,s]  for p,s in zip(position,speed)]
        for p,s in sorted(pairs)[::-1]:
            stack.append( (target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        