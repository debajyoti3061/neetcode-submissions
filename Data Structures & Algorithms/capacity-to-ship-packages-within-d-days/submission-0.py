"""
REVISION NOTES - Capacity To Ship Packages Within D Days:
- Binary search on capacity (min = max weight, max = sum of weights)
- For each capacity, simulate shipping to check if feasible
- If can ship within days, try smaller capacity
- Otherwise, need larger capacity
- Time: O(n log(sum)), Space: O(1)
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights), sum(weights)
        res = r
        
        def canShip(cap: int) -> bool:
            ships , curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -= w
            return True



        while l <= r:
            mid = (l+r)//2    
            if canShip(mid):
                r = mid-1
                res = min(res,mid)
            else:
                l = mid +1
        
        return res


        