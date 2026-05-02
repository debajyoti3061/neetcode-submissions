"""
REVISION NOTES - Merge Strings Alternately:
• Use two pointers to traverse both strings simultaneously
• Alternate between characters from word1 and word2
• Continue until one string is exhausted
• Append remaining characters from longer string
• Use list for efficient string building, then join at end
• Time: O(m+n), Space: O(m+n)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j =  0
        res  = []
        while i < len(word1) and j < len(word2):
            res.append( word1[i])
            res.append( word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
            