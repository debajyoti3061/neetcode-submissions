"""
REVISION NOTES - Search For Word (Word Search):
• DFS backtracking to find word in 2D board
• Try starting from each cell that matches first character
• Use DFS to explore all 4 directions for remaining characters
• Mark current cell as visited (use temp variable) to avoid revisiting
• Backtrack by restoring original character after exploring
• Return True if complete word is found, False otherwise
• Time: O(m*n*4^L), Space: O(L) where L is word length
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(board,i,j, index):
            if i <0 or j <0 or i >= len(board) or j >= len(board[i]) or board[i][j] != word[index]:
                return False
            if index == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = " "
            found = dfs(board,i+1,j, index+1) or dfs(board,i-1,j, index+1) or dfs(board,i,j+1, index+1) or dfs(board,i,j-1, index+1)
            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(board,i,j,0):
                    return True
        return False

        