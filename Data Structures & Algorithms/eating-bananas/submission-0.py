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


        