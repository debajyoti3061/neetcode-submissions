"""
REVISION NOTES - Maximum Product Subarray:
- Track both maximum and minimum products ending at each position
- Negative numbers can make minimum become maximum
- For each element: new_max = max(num, max_prod * num, min_prod * num)
- Update global maximum at each step
- Time: O(n), Space: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1 , 1
        res = nums[0]
        for num in nums:
            
            tmp = curMax * num
            curMax = max(curMax * num,curMin * num, num)
            curMin = min(tmp,curMin * num, num)
            res = max(res,curMax)
        return res
        