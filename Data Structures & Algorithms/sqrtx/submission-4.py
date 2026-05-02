"""
REVISION NOTES - Sqrt(x):
• Binary search approach to find integer square root
• Search range from 0 to x, find largest integer whose square ≤ x
• Keep track of result when m*m < x (potential answer)
• When m*m > x, search left half; when m*m < x, search right half
• Return exact match if found, otherwise return last valid result
• Time: O(log x), Space: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = (l+r)//2
            if m*m > x:
                r = m-1
            elif m*m < x:
                l = m+1
                res = m
            else:
                return m
        return res
        