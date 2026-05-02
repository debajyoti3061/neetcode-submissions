"""
REVISION NOTES - Coin Change Ii:
- Use DP or DFS with memoization to count combinations
- For each coin, decide to include or exclude it
- Memoize on (coin_index, remaining_amount)
- Base cases: amount = 0 (return 1), no coins left (return 0)
- Time: O(coins * amount), Space: O(coins * amount)
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remain):
            if remain == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, remain) in memo:
                return memo[(i, remain)]

            res = dfs(i + 1, remain)
            if remain >= coins[i]:
                res += dfs(i, remain - coins[i])

            memo[(i, remain)] = res
            return res

        return dfs(0, amount)