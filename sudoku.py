import math
import time


#check column
def check_column(i , j , grid,value):
    print('i = ',i)
    print('j= ', j)
    for x in range(n):
        print('x=',x)
        if x == j:
            print('this cell')
            pass
        elif grid[i][x] == value:
            print('fail')
            return False
        
def check_row(i , j ,grid,value):
    for y in range(n):
        print('y=',y)
        if y == i:
            print('this cell')
            pass
        elif grid[y][j] == value:
            print('y=',y,'j=',j,'value=',value)
            print('fail')
            return False
        
def check_box(i , j , grid,value):
    box_i = (i // int(math.sqrt(n))) * int(math.sqrt(n))
    box_j = (j // int(math.sqrt(n))) * int(math.sqrt(n))
    print('box-i=',box_i)
    print('box-j=',box_j)
    print('step = ', math.sqrt(n)-1)
    for x in range(box_i, box_i + int(math.sqrt(n))-1):
        for y in range(box_j, box_j + int(math.sqrt(n))-1):
            print('x in  box =',x)
            print('y in box=',y)
            if x==i & y ==j:
                pass
            elif grid[x][y] == value:
                return False
            
# Define helper function to check if a value is valid in a given position
def is_valid(i, j, value , grid):
    # Check row
    validation_row = check_row(i , j , grid,value)
    if validation_row == False:
        return False
    else:
        # Check column
        validation_column = check_column(i , j , grid,value)
        if validation_column == False:
            return False
        else:
            validation_box = check_box(i , j ,grid,value)
            if validation_box == False:
                return False
            else:
                # Value is valid
                return True

# Print solution
def prin_solution(grid):
    for row in grid:
        print(' '.join(str(x) for x in row))

# Define recursive function to solve Sudoku grid     
def solve(i, j , grid):
        print('(i',i,'j',j,')')
        # Base case: end of grid
        if i == n:
            return True
        # Calculate next position
        next_i = i if j < n - 1 else i + 1
        next_j = (j + 1) % n
        # Check if position is already filled
        print('check position is filled')
        if grid[i][j] != 0:
            return solve(next_i, next_j,grid)
        # Try all possible values for current position
        print('try possible values')
        for value in range(1, n+1):
            print('value = ', value)
            print('i',i,'j',j)
            if is_valid(i, j, value,grid):
                grid[i][j] = value
                if solve(next_i, next_j,grid):
                    return True
                grid[i][j] = 0
        # No valid value found, backtrack
        return False

def solve_sudoku(n, c, board):
    # Create empty grid
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Fill in given values
    for i, j, value in board:
        grid[i][j] = value
        print('i=',i,',j=',j,', value= ',value)

    # Solve grid
    if solve(0, 0 , grid):
        # Print solution
        prin_solution(grid)
    else:
        print('Unsolvable csp!')


# Example usage

n = int(input("Enter the size of the Sudoku grid: "))
c = int(input("Enter the number of filled cells in the Sudoku grid: "))
print('for the next ',c,' line enter the number of row, column and value seperated by one space')
board = []
for _ in range(c):
    i, j, value = map(int, input().split())
    print('i=',i,' j=',j)
    board.append((i-1, j-1, value))

solve_sudoku(n , c, board)
