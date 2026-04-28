class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            offset = (columnNumber-1) % 26
            res += chr(ord('A')+ offset)
            columnNumber = (columnNumber-1) // 26

        return res[::-1]
        