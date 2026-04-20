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
        