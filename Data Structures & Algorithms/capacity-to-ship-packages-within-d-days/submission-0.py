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


        