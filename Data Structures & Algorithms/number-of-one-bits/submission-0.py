"""
REVISION NOTES - Number Of One Bits:
- Use bit manipulation to count set bits
- Method 1: Check each bit using n & 1, then right shift
- Method 2: Use n & (n-1) to clear rightmost set bit
- Continue until n becomes 0
- Time: O(log n), Space: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n >> 1
        return res
        