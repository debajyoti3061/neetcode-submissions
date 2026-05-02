"""
REVISION NOTES - Count Paths:
- dp[i][j] = number of paths to reach cell (i,j)
- Can only move right or down
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Initialize first row and column to 1
- Time: O(m*n), Space: O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range (m)]
        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]