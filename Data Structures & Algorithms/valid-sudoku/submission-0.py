class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        attempt without conceptiual part of the video 
        rows = {}
        cols = {}
        boxes = {}
        for i in range(len(board)):
            cols[board[i][i]] = 1 + cols.get(board[i][i])
            for j in range(len(board(i))):
                rows[board[i][j]] = 1 + cols.get(board([i][j]))


        # attempt with conceptual couldn't quite figure out the box method 
        boxes = {}
        box = set()
        for i in range(len(board)):
            ind_rows = set()
            ind_cols = set()
            
            for j in range(len(board)):
                current_box = (i//3, j//3)
                if board[i][j] in ind_rows and board[i][j] is int:
                    return False
                elif board[j][i] in ind_cols and board[j][i] is int: 
                    return False
                elif ((board[i][j] or board[j][i]) in (boxes.get(current_box) or box)) and (board[i][j] or board[j][i]) is int:
                    return False
                else:
                    ind_rows.add(board[i][j])
                    ind_cols.add(board[j][i])
                    boxes[current_box] = box.add(board[i][j])
                    boxes[current_box] = box.add(board[j][i])
        return True 
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True 




            