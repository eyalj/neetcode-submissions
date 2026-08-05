class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rows = {i:False for i in range(10)}
            for item in row:
                if(item == "."):
                    continue
                item = int(item)
                if rows[item]:
                    return False
                else:
                    rows[item] = not rows[item]

        for i in range(len(board)):
            col = {i:False for i in range(10)}
            for j in range(len(board[i])):
                if(board[j][i] == "."):
                    continue
                item = int(board[j][i])
                if col[item]:
                    return False
                else:
                    col[item] = not  col[item]

        for box_number_in_row in range (0,3):
            for box_number_in_col in range (0,3):
                box = {i: False for i in range(10)}            
                for i in range(0,3):
                    for j in range(0,3):
                        index_i = i+3*box_number_in_row
                        index_j = j+3*box_number_in_col
                        item = board[index_j][index_i]
                        if(item == '.'):
                            continue
                        item = int(item)
                        if box[item]:
                            return False
                        else: box[item] = not box[item]

        return True



        