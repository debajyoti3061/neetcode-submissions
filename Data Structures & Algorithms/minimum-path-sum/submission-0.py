"""
REVISION NOTES - Minimum Path Sum:
• Dynamic programming: modify grid in-place to store minimum path sums
• For each cell, add minimum of path from top or left
• Handle edge cases: first row (only from left), first column (only from top)
• grid[i][j] represents minimum sum to reach cell (i,j)
• Return bottom-right cell which contains minimum path sum
• Time: O(m*n), Space: O(1)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
        