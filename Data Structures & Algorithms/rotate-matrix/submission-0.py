"""
REVISION NOTES - Rotate Matrix:
• Rotate matrix 90 degrees clockwise in-place using layer-by-layer approach
• Process matrix from outer layer to inner layer (l to r pointers)
• For each layer, rotate 4 elements at a time in a cycle
• Save top-left, then move: bottom-left → top-left → top-right → bottom-right → bottom-left
• Continue for all positions in current layer, then move to inner layer
• Time: O(n²), Space: O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l): 
                top, bottom = l, r
                topLeft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r]= topLeft
        
            l += 1
            r -= 1

        