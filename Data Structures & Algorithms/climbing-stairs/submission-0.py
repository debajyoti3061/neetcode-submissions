"""
REVISION NOTES - Climbing Stairs:
• Each step can be reached from previous step or step before that
• dp[i] = dp[i-1] + dp[i-2]
• Base cases: dp[1] = 1, dp[2] = 2
• Can optimize space to O(1) using two variables
• Time: O(n), Space: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        