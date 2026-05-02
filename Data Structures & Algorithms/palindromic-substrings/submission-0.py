"""
REVISION NOTES - Palindromic Substrings:
• Expand around centers approach to count all palindromic substrings
• For each position, check for odd-length palindromes (center at i)
• Also check for even-length palindromes (center between i and i+1)
• Expand outward while characters match and count valid palindromes
• Sum counts from all possible centers
• Time: O(n²), Space: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPal(s,i,i)
            res += self.countPal(s,i,i+1)
        return res

    def countPal(self,s,i,j):
        res = 0
        while i >= 0 and j < len(s) and s[i]==s[j]:
            res += 1
            i -= 1
            j += 1
        return res
        