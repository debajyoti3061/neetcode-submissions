class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0] 


       # i, j = 0, 0
       # lcs = []

       # while i < len(text1) and j < len(text2):
       #     if text1[i] == text2[j]:
       #         lcs.append(text1[i])
       #         i += 1
       #         j += 1
       #     elif dp[i+1][j] > dp[i][j+1]:
       #         i += 1
       #     else:
       #         j += 1

       # return "".join(lcs)       