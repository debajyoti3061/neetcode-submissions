"""
REVISION NOTES - Valid Palindrome II:
• Two-pointer approach with one deletion allowed
• Start from both ends, when mismatch found: try skipping left OR right character
• Helper function checks if substring is palindrome without further deletions
• Key insight: at most one deletion means we have two choices when mismatch occurs
• If either choice (skip left or skip right) results in palindrome, return True
• Time: O(n), Space: O(1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j :
            if s[i] != s[j] :
                return self.isPalindrome(s,i+1,j) or self.isPalindrome(s,i,j-1)
            i += 1
            j -= 1
        return True
    

    def isPalindrome(self, s: str, i: int, j: int) -> bool :
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
