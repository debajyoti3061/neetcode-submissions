"""
REVISION NOTES - Islands And Treasure:
• Multi-source DFS: start from all treasure gates (value 0) simultaneously
• For each gate, use DFS to propagate distances to all reachable empty rooms
• Only update a cell if current distance is smaller than existing value
• This ensures shortest distance from any gate is stored
• Stop DFS when hitting walls (-1) or already shorter distances
• Time: O(m*n), Space: O(m*n) for recursion stack
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(grid,i,j,count):
            if i < 0 or j <0 or i>= len(grid) or j >= len(grid[i]) or grid[i][j] < count:
                return
            grid[i][j] = count
            dfs(grid,i+1,j, count+1)
            dfs(grid,i-1,j, count+1)
            dfs(grid,i,j+1, count+1)
            dfs(grid,i,j-1, count+1)



        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(grid,i,j,0)
        