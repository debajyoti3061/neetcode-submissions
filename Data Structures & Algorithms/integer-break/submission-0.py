"""
REVISION NOTES - Integer Break:
• Dynamic programming: dp[i] = maximum product for breaking number i
• For target number n, dp[n] starts at 0 (must break it)
• For other numbers, dp[i] can be i itself (no breaking) or broken further
• Try all possible splits: i = j + (i-j), take max of dp[j] * dp[i-j]
• Build up from smaller numbers to larger ones
• Time: O(n²), Space: O(n)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        for num in range(2,n+1):
            dp[num] = 0 if num == n else num
            for i in range(1,num):
                val = dp[i] * dp[num-i]
                dp[num] = max(dp[num],val)
        return dp[n]
        