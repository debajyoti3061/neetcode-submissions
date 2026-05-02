"""
REVISION NOTES - Best Time To Buy And Sell Stock Ii:
- Greedy approach: capture every profitable transaction
- For each day, if price > previous day, add profit
- Can buy and sell on same day (no transaction cost)
- Sum all positive price differences
- Time: O(n), Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
        