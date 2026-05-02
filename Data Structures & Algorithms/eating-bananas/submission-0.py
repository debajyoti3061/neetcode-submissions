"""
REVISION NOTES - Eating Bananas:
- Binary search on eating speed (1 to max pile size)
- For each speed, calculate total hours needed
- If hours <= h, try smaller speed; otherwise try larger speed
- Find minimum speed that allows finishing within h hours
- Time: O(n log m), Space: O(1)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                r = k - 1
                res = min(res,k)
            else:
                l = k+1
        return res


        