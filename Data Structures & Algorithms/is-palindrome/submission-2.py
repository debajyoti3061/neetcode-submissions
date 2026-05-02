"""
REVISION NOTES - Is Palindrome:
• Two-pointer approach: start from both ends and move inward
• Skip non-alphanumeric characters using isalnum() check
• Compare characters case-insensitively using lower()
• If any mismatch found, return False
• If all comparisons pass, string is a palindrome
• Time: O(n), Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
    # Now compare s[i] and s[j] safely
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        