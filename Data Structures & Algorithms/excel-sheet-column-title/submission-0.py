"""
REVISION NOTES - Excel Sheet Column Title:
- Convert number to Excel column title (base 26 with A-Z)
- Use modulo and division to extract digits
- Handle 1-indexed system (subtract 1 before modulo)
- Build result string from right to left
- Time: O(log n), Space: O(log n)
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            offset = (columnNumber-1) % 26
            res += chr(ord('A')+ offset)
            columnNumber = (columnNumber-1) // 26

        return res[::-1]
        