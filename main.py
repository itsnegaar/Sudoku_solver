import numpy as np
import time
from solver_mrv_lcv import *
from solver import *
from utils import *

if __name__ == "__main__":
    
    # Read input from user
    print('here')
    n = int(input('Enter the size of the grid.').strip())  # size of the board
    c = int(input('Enter the number of filled cells.').strip())  # number of cells to fill
    print('board')
    # Initialize the board with zeros
    board = [[0] * n for _ in range(n)]

    # Fill in the cells with given values
    print('in the next ', c , ' lines, Enter i,j, value of filled cell.')
    for _ in range(c):
        i, j, value = map(int, input().strip().split())
        board[i-1][j-1] = value


    '''# Read input from twxt file
    # Open the file and read the contents
    with open('test_case.txt', 'r') as f:
        lines = f.readlines()

    # Get the board size and initialize the board
    n = int(lines[0])
    board = [[0] * n for _ in range(n)]

    # Fill in the constant values
    for i in range(2, int(lines[1]) + 2):
        row, col, val = map(int, lines[i].split())
        board[row][col] = val '''

    start_time = time.time()
    if solve_sudoku(board):
        print('solvable')
        print_board(board)
    else:
        print("Unsolvable CSP!")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")


    start_time_op = time.time()
    if solve_sudoku_optimized(board):
        print('solvable')
        print_board(board)
    else:
        print("Unsolvable CSP!")

    end_time_op = time.time()
    elapsed_time_op = end_time_op - start_time_op

    print(f"Elapsed time optimized: {elapsed_time_op} seconds")
