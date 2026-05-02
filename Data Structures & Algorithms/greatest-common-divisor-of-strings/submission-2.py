"""
REVISION NOTES - Greatest Common Divisor Of Strings:
• Try all possible divisor lengths from largest to smallest
• For each length, check if it divides both string lengths evenly
• Verify that repeating the substring creates both original strings
• Return first valid divisor (which will be the largest/greatest)
• If no divisor found, return empty string
• Time: O(min(m,n) * (m+n)), Space: O(1)
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""