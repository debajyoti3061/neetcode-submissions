"""
REVISION NOTES - Longest Common Prefix:
• Use first string as reference, compare character by character
• For each position i, check if all strings have same character at position i
• Stop when any string is shorter or has different character
• Return prefix up to the mismatch point
• If no mismatch found, entire first string is the common prefix
• Time: O(S) where S is sum of all characters, Space: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
        