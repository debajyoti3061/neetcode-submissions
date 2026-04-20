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

        