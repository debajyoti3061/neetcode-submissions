"""
REVISION NOTES - Edit Distance:
- Use 2D DP: dp[i][j] = min edits to transform word1[0:i] to word2[0:j]
- If characters match: dp[i][j] = dp[i-1][j-1]
- If don't match: dp[i][j] = 1 + min(insert, delete, replace)
- Initialize base cases for empty strings
- Time: O(m*n), Space: O(m*n)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range (1,len(dp)):
            for j in range(1,len(dp[0])):
                if word1[i-1] == word2[j-1] :
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[m][n]
        