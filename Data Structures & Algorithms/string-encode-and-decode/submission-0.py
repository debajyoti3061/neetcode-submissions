"""
REVISION NOTES - String Encode and Decode:
• Length-prefixed encoding: format is "length#string" for each string
• Encode: concatenate length + "#" + string for each input string
• Decode: parse length before "#", then extract exact number of characters
• Handles edge cases like empty strings and strings containing "#"
• Key insight: use length prefix to avoid delimiter conflicts
• Time: O(n) for both encode/decode, Space: O(1) extra
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


