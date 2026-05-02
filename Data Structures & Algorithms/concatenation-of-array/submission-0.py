"""
REVISION NOTES - Concatenation Of Array:
- Create result array of size 2*n
- Fill both halves with original array elements
- Use single loop with modulo operation for efficiency
- Time: O(n), Space: O(n)
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * (2*len(nums))
        for i,num in enumerate(nums) :
            output[i] = output[i+len(nums)] = num
        return output
        