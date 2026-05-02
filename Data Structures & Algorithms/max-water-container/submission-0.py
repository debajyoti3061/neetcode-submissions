"""
REVISION NOTES - Max Water Container:
- Use two pointers from both ends of array
- Calculate area with current pointers, update maximum
- Move pointer with smaller height inward
- Continue until pointers meet
- Time: O(n), Space: O(1)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j = 0, len(heights)-1
        total = 0
        while i < j:
            total = max(total, min(heights[i],heights[j])* (j-i))
            if heights[i] < heights[j] :
                i += 1
            else :
                j -= 1
        return total
        