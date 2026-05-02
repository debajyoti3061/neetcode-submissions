"""
REVISION NOTES - Decode Ways:
- Use DP: dp[i] = ways to decode string[0:i]
- Check single digit (1-9) and double digit (10-26) decodings
- dp[i] = dp[i-1] (if valid single) + dp[i-2] (if valid double)
- Handle edge cases with '0'
- Time: O(n), Space: O(n)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0]  = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2,n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i-1]
            if 10 <= second <= 26:
                dp[i] += dp[i-2]
        return dp[n]

        