"""
REVISION NOTES - Bitwise And Of Numbers Range:
- Find common prefix of left and right in binary
- Right shift both numbers until they're equal
- Left shift back to get the result
- All bits after common prefix will become 0
- Time: O(log n), Space: O(1)
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i