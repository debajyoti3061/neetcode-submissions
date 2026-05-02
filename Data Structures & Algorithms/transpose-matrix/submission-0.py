"""
REVISION NOTES - Transpose Matrix:
• Create new matrix with swapped dimensions (COLS x ROWS)
• Key transformation: element at matrix[i][j] goes to result[j][i]
• Initialize result matrix with correct dimensions first
• Iterate through original matrix and place elements in transposed positions
• Simple coordinate transformation problem
• Time: O(m*n), Space: O(m*n) for result matrix
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0]* ROWS for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                res[j][i] = matrix[i][j]
        
        return res
        