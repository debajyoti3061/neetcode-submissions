"""
REVISION NOTES - House Robber Ii:
- Houses arranged in circle, so first and last can't both be robbed
- Solve two subproblems: rob houses 0 to n-2, and houses 1 to n-1
- Return maximum of both solutions
- Use House Robber I solution for each subproblem
- Time: O(n), Space: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[1], dp[0])
            
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(helper(nums[:n-1]), helper(nums[1:]))