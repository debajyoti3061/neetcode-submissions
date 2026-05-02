"""
REVISION NOTES - N-th Tribonacci Number:
• Dynamic programming: each number is sum of previous three numbers
• Base cases: T(0)=0, T(1)=1, T(2)=1
• Use DP array to store computed values and avoid recomputation
• Build up from base cases to target number n
• Alternative: space-optimized version using only 3 variables
• Time: O(n), Space: O(n)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n== 1: return 1
        elif n== 2: return 1
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0,1,1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
        