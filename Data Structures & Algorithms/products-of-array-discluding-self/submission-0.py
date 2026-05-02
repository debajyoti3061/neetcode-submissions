"""
REVISION NOTES - Products Of Array Discluding Self:
- Calculate prefix products from left to right
- Calculate suffix products from right to left while building result
- Multiply prefix and suffix products for each position
- Avoid division to handle zeros correctly
- Time: O(n), Space: O(1) excluding output array
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        