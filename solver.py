import numpy as np
from utils import find_empty_cell, is_valid_move

#solve sudoku
def solve_sudoku(board):
    #if there is no empty cell left, return true
    if not find_empty_cell(board):
        return True
    
    #for empty cells try possible variables
    row, col = find_empty_cell(board)
    for value in range(1, len(board)+1):
        if is_valid_move(board, row, col, value):
            board[row][col] = value
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
        
    return False
