"""
REVISION NOTES - Longest Substring Without Duplicates:
• Use sliding window with set to track characters in current window
• Expand right pointer and add characters to set
• When duplicate found, shrink left pointer until duplicate removed
• Track maximum window size seen
• Time: O(n), Space: O(min(m,n)) where m is charset size
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r-l+1)
        return result

        