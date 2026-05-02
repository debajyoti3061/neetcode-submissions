"""
REVISION NOTES - Jump Game Ii:
- Use greedy approach to find minimum jumps
- Track current jump's reach and farthest possible reach
- When current reach is exhausted, make another jump
- Count number of jumps needed
- Time: O(n), Space: O(1)
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curFurthest = 0, 0 , 0
        for i in range(len(nums)-1):
            curFurthest = max(curFurthest, i+nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFurthest
        
        return jumps