"""
REVISION NOTES - Count Number of Islands:
• Use DFS or BFS to explore connected components
• For each unvisited land cell, start DFS and mark all connected land
• Increment island count for each DFS start
• Mark visited cells to avoid recounting
• Time: O(m*n), Space: O(m*n)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        def dfs(grid, i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] =="0":
                return 0
            
            grid[i][j] = "0"
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            return 1


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    result += dfs(grid,i,j)
        return result

        