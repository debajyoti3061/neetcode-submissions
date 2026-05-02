"""
REVISION NOTES - Minimum Size Subarray Sum:
• Sliding window approach with two pointers
• Expand window by moving right pointer, add elements to total
• When total >= target, try to shrink window from left
• Track minimum window size that satisfies condition
• Continue until right pointer reaches end
• Time: O(n), Space: O(1)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0 , 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r-l+1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res



        