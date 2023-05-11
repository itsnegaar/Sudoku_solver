import numpy as np
def print_board(grid):
    for row in grid:
        print(*row)


#find emty cell
def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


#check the validation of value
def is_valid_move(board, row, col, value):
    # check if value is already in the row
    if value in board[row]:
        return False
    
    # check if value is already in the column
    if value in [board[i][col] for i in range(len(board))]:
        return False
    
    # check if value is already in the sub-grid
    subgrid_row = (row // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    subgrid_col = (col // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    
    for i in range(subgrid_row, subgrid_row + int(np.sqrt(len(board)))):
        for j in range(subgrid_col, subgrid_col + int(np.sqrt(len(board)))):
            if board[i][j] == value:
                return False
            
    return True


#give all possible values
def get_valid_moves(board, row, col):
    moves = set(range(1, len(board)+1))
    
    # remove values already in the row
    moves -= set(board[row])
    
    # remove values already in the column
    moves -= set([board[i][col] for i in range(len(board))])
    
    # remove values already in the sub-grid
    subgrid_row = (row // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    subgrid_col = (col // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    
    for i in range(subgrid_row, subgrid_row + int(np.sqrt(len(board)))):
        for j in range(subgrid_col, subgrid_col + int(np.sqrt(len(board)))):
            moves.discard(board[i][j])
    
    return moves

