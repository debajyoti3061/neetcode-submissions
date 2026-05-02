"""
REVISION NOTES - Partition Equal Subset Sum:
• Dynamic programming subset sum problem
• If total sum is odd, impossible to partition equally
• Target is half of total sum - check if subset with this sum exists
• Use 1D DP array where dp[i] = True if sum i is achievable
• Process numbers in reverse order to avoid using same number twice
• Time: O(n * sum), Space: O(sum)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]