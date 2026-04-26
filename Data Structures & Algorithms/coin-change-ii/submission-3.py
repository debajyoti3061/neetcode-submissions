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