import re
import os
import time
from SudokuGenerator import SudokuAPI

class grid:
    def __init__(self, grid: list[list, list, list, list, list, list, list, list, list] = None, counter:int = 0):
        self.grid = grid
        self.grid = [[0, 0, 0, 0, 0, 0, 6, 0, 0],
                     [0, 3, 0, 2, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 8, 0, 0],
                     [0, 0, 6, 0, 8, 9, 2, 0, 1],
                     [0, 0, 8, 0, 0, 3, 0, 6, 0],
                     [3, 0, 0, 0, 0, 0, 5, 7, 8],
                     [0, 0, 0, 0, 3, 0, 9, 0, 2],
                     [9, 5, 4, 8, 7, 2, 3, 0, 0]]
        self.counter = 0
        for i in self.grid:
            self.counter += len(list(filter(lambda x: x == 0, i)))
    
    def __repr__(self):
        strGrid = ''
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    strGrid += f'| \033[30m{self.grid[i][j]}\033[30m '
                else:
                    strGrid += '| \033[31m0\033[30m '
                if j == 8:
                    strGrid += '\033[30m|\033[30m'
            if i != 8:
                strGrid += '\n'
        os.system('cls')
        return strGrid
    
    def initiate(self):
        #row1
        row1input = input('''What numbers are in the top row?\n
                  Please use 0 as a placeholder and answer in a list of integers with spaces in between them.\n\n--> ''')
        self.counter += len(re.findall(r'0', row1input))
        row1 = row1input.split(row1input.strip())
        
        #row2
        row2input = input("Please do the same with the second row\n--> ")
        self.counter += len(re.findall(r'0', row2input))
        row2 = row2input.split(row2input.strip())
        
        #row3
        row3input = input("Please do the same with the third row\n--> ")
        self.counter += len(re.findall(r'0', row3input))
        row3 = row3input.split(row3input.strip())
        
        #row4
        row4input = input("Please do the same with the fourth row\n--> ")
        self.counter += len(re.findall(r'0', row4input))
        row4 = row4input.split(row4input.strip())
        
        #row5
        row5input = input("Please do the same with the fifth row\n--> ")
        self.counter += len(re.findall(r'0', row5input))
        row5 = row5input.split(row5input.strip())
        
        #row6
        row6input = input("Please do the same with the sixth row\n--> ")
        self.counter += len(re.findall(r'0', row6input))
        row6 = row6input.split(row6input.strip())
        
        #row7
        row7input = input("Please do the same with the seventh row\n--> ")
        self.counter += len(re.findall(r'0', row7input))
        row7 = row7input.split(row7input.strip())
        
        #row8
        row8input = input("Please do the same with the eighth row\n--> ")
        self.counter += len(re.findall(r'0', row8input))
        row8 = row8input.split(row8input.strip())
        
        #row9
        row9input = input("Please do the same with the ninth row\n--> ")
        self.counter += len(re.findall(r'0', row9input))
        row9 = row9input.split(row9input.strip())
        
        self.grid = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    def ifPossible(self, i, j):
        # Initialize sets for row, column, and square
        row = set(self.grid[i])
        column = set(self.grid[k][j] for k in range(9))
        
        # Determine the square based on the indices
        square_row = (i // 3) * 3
        square_col = (j // 3) * 3
        square = set(
            self.grid[m][n]
            for m in range(square_row, square_row + 3)
            for n in range(square_col, square_col + 3)
        )
        
        # Find valid numbers (1-9) that are not in row, column, or square
        all_numbers = set(range(1, 10))
        invalid_numbers = row | column | square
        options = list(all_numbers - invalid_numbers)
        print(self, end='\r')
        
        # If only one valid number exists, update the grid
        if len(options) == 1:
            self.grid[i][j] = options[0]
            return None  # Signal that progress was made
        return options  # Return the list of valid options

sudoku_api = SudokuAPI(difficulty="hard")  # Change difficulty to "easy", "medium", or "hard" as needed
board1 = sudoku_api.fetch_board()
board = grid(board1)

while board.counter > 0:
    for i in range(9):
        for j in range(9):
            if board.grid[i][j] == 0:
                ifNull = board.ifPossible(i, j)
                if ifNull is None:
                    board.counter -= 1
                os.system('cls')
                print(repr(board), board.counter, ifNull, end='\r')
                time.sleep(0.1)