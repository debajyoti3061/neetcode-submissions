"""
REVISION NOTES - Reverse Bits:
- Process each bit from right to left
- Extract bit using n & 1, add to result
- Shift result left and n right for next iteration
- Continue for all 32 bits
- Time: O(1), Space: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31-i)
        return res
        