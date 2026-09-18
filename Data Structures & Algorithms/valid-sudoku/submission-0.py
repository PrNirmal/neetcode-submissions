class Solution:
    def rowChecked(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=[j for j in board[i] if j!="."]
            has_duplicate=len(s)!=len(set(s))
            if has_duplicate:
                return False
        return True
        

    def columnChecked(self, board: List[List[str]]) -> bool:
        for j in range(9):
            col=[]
            for i in range(9):
                if board[i][j]!=".":
                    if board[i][j] not in col:
                        col.append(board[i][j])
                    else:
                        return False
        return True
            
    def cell_checked(self, board: List[List[str]]) -> bool:

        end_row=0
        end_col=0
        while end_row<=6:
            col=[]
            for i in range(end_row,end_row+3):

                for j in range(end_col,end_col+3):
                    if board[i][j]!=".":
                        if board[i][j] not in col:
                            col.append(board[i][j])
                        else:
                            return False
            end_col+=3
            if end_col>6:
                end_col=0
                end_row+=3


        return True
            


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rowChecked(board) and self.columnChecked(board) and self.cell_checked(board)
        