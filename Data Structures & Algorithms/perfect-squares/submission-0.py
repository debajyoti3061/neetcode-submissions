"""
REVISION NOTES - Perfect Squares:
• Dynamic programming: dp[i] = minimum number of perfect squares that sum to i
• Initialize dp array with worst case (all 1s), dp[0] = 0
• For each target, try all possible perfect squares less than or equal to target
• dp[target] = min(dp[target], 1 + dp[target - square])
• Build up from smaller numbers to target n
• Time: O(n * √n), Space: O(n)
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1,n+1):
            for s in range(1,target+1):
                square = s*s
                if (target-square) < 0:
                    break
                dp[target] = min(dp[target],1+ dp[target-square])

        return dp[n] 
        