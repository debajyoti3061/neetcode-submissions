"""
REVISION NOTES - Valid Sudoku:
• Single pass validation using set to track seen values
• Create unique identifiers for each constraint: row, column, and 3x3 box
• For each non-empty cell, generate three strings: "value in row i", "value in column j", "value in box xy"
• Box index calculated as (i//3, j//3) to identify which 3x3 subgrid
• If any identifier already exists in set, sudoku is invalid
• Add all three identifiers to set for future checks
• Time: O(1) since board is fixed 9x9, Space: O(1)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    row = board[i][j] + " in row " + str(i)
                    column = board[i][j] + " in column " + str(j)
                    box = board[i][j] + " in box " + str(i//3) + str(j//3)
                    if row in set1 or column in set1 or box in set1:
                        return False
                    set1.add(row)
                    set1.add(column)
                    set1.add(box)
        return True

        