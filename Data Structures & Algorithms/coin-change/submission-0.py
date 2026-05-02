"""
REVISION NOTES - Coin Change:
• dp[i] = minimum coins needed to make amount i
• For each amount, try all coin denominations
• dp[i] = min(dp[i], 1 + dp[i - coin]) for each valid coin
• Return dp[amount] or -1 if impossible
• Time: O(amount * coins), Space: O(amount)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1
        