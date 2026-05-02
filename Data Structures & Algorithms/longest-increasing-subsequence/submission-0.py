"""
REVISION NOTES - Longest Increasing Subsequence:
- dp[i] = length of LIS ending at index i
- For each element, check all previous smaller elements
- dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
- Return maximum value in dp array
- Time: O(n^2), Space: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range (i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
        