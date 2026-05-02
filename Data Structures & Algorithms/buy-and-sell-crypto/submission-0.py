"""
REVISION NOTES - Best Time to Buy and Sell Stock:
- Use two pointers: buy (left) and sell (right)
- Track minimum price seen so far as potential buy point
- Calculate profit at each step and update maximum
- Move buy pointer when current price is lower
- Time: O(n), Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices) :
            if prices[l] < prices[r] :
                maxP = max (maxP, prices[r] - prices[l])
            else :
                l = r

            r += 1
        return maxP
        