from utils import find_empty_cell, is_valid_move
import numpy as np

def mrv(board):
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_cells.append((i, j))
                
    return min(empty_cells, key=lambda x: len(get_valid_moves(board, x[0], x[1])))

def lcv(board, row, col):
    moves = list(get_valid_moves(board, row, col))
    return sorted(moves, key=lambda x: len(get_valid_moves(board, row, col) - set([x])))

def forward_check(board, row, col, value):
    subgrid_row = (row // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    subgrid_col = (col // int(np.sqrt(len(board)))) * int(np.sqrt(len(board)))
    
    for i in range(subgrid_row, subgrid_row + int(np.sqrt(len(board)))):
        for j in range(subgrid_col, subgrid_col + int(np.sqrt(len(board)))):
            if board[i][j] == value:
                return False
            
            if board[i][j] == 0 and not get_valid_moves(board, i, j).difference({value}):
                return False
        
    return True

def solve_sudoku_optimized(board):
    if not find_empty_cell(board):
        return True
    
    row, col = mrv(board)
    for value in lcv(board, row, col):
        if is_valid_move(board, row, col, value):
            board[row][col] = value
            
            if forward_check(board, row, col, value) and solve_sudoku_optimized(board):
                return True
            
            board[row][col] = 0
        
    return False


