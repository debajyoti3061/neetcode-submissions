"""
REVISION NOTES - Search 2D Matrix:
• Two-phase binary search approach
• Phase 1: Binary search on rows to find correct row
• Compare target with first and last element of each row
• Phase 2: Binary search within the identified row
• Leverages sorted property of both rows and columns
• Alternative: Treat as 1D array with coordinate mapping
• Time: O(log m + log n), Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        if not (top <= bot):
            return False
        mid = (top+bot)//2
        l , r = 0, cols-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False
        