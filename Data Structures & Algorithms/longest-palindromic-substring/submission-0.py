"""
REVISION NOTES - Longest Palindromic Substring:
- Expand around centers approach (odd and even length palindromes)
- For each position, expand outward while characters match
- Track longest palindrome found so far
- Handle both odd-length and even-length palindromes
- Time: O(n^2), Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resInd = 0
        resLen = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resInd = l
                    resLen = r-l+1
                l -= 1
                r += 1

            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resInd = l
                    resLen = r-l+1
                l -= 1
                r += 1
        return s[resInd:resLen+resInd]
        