"""
REVISION NOTES - Find K Closest Elements:
• Use two pointers (left, right) to shrink window to size k
• Compare distances from x to elements at both ends
• Remove the element that's farther from x (or right if equal distance)
• Continue until window size equals k
• Time: O(n-k), Space: O(1)
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0, len(arr)-1
        while r-l >= k:
            if abs(arr[l] - x) <= abs(arr[r] -x):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]
        