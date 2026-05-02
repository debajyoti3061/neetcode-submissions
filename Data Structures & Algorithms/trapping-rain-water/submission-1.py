"""
REVISION NOTES - Trapping Rain Water:
• Use two pointers with left_max and right_max tracking
• Move pointer with smaller max value inward
• Add trapped water based on difference between max and current height
• Water trapped depends on minimum of left and right boundaries
• Time: O(n), Space: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l , r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax :
                l += 1
                leftMax = max(leftMax,height[l])
                res += leftMax-height[l]

            else :
                r -= 1
                rightMax = max(rightMax,height[r])
                res += rightMax-height[r]
        return res

        
        