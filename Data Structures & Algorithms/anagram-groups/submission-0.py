"""
REVISION NOTES - Anagram Groups:
• Sort each string to create a key for grouping anagrams
• Use hashmap where key is sorted string, value is list of original strings
• All anagrams will have the same sorted representation
• Return list of all grouped values
• Time: O(n * m log m), Space: O(n * m)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            charArray = [a for a in s]
            charArray.sort()
            tempString = ('').join(charArray)
            if tempString not in map:
                map[tempString] = []
            map[tempString].append(s)
        return list(map.values())
        