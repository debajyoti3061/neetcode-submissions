"""
REVISION NOTES - Jump Game:
- Track the farthest position reachable so far
- For each position, update farthest if current position is reachable
- If farthest reaches or exceeds last index, return true
- If current position > farthest, return false
- Time: O(n), Space: O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        