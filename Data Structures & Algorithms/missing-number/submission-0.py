"""
REVISION NOTES - Missing Number:
- Use XOR or sum formula approach
- XOR: XOR all numbers 0 to n with all array elements
- Sum: expected_sum - actual_sum = missing number
- Both handle overflow differently
- Time: O(n), Space: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for num in nums:
            res += num
        total = n * (n+1)/2
        return int(total-res)
        
        