"""
REVISION NOTES - Is Anagram:
- Sort both strings and compare, or use character frequency count
- Two strings are anagrams if they have same character frequencies
- Can use array of size 26 for lowercase letters
- Time: O(n log n) for sorting, O(n) for counting
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
        return True

        