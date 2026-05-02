"""
REVISION NOTES - Longest Repeating Substring With Replacement:
• Sliding window with character frequency tracking
• Expand window by moving right pointer, count character frequencies
• Window is valid if (window_size - max_frequency) <= k
• When invalid, shrink window from left until valid again
• Track maximum valid window size seen
• Time: O(n), Space: O(1) - at most 26 characters
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
        