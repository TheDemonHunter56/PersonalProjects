import os
from SudokuGenerator import SudokuAPI

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.counter = 0

    def is_valid(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False

        # Check column
        if num in [self.grid[r][col] for r in range(9)]:
            return False

        # Check 3x3 square
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.grid[r][c] == num:
                    return False

        return True

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

    def solve(self):
        # Find the next empty cell
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    # Try numbers 1-9
                    for num in range(1, 10):
                        self.counter += 1
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.counter % 1000 == 0:
                                os.system("cls")
                                print(self)  # Show the grid after placement

                            if self.solve():  # Recurse
                                return True
                            
                            self.grid[row][col] = 0  # Backtrack
                            if self.counter % 100000 == 0:
                                os.system("cls")
                                print(self)# Show the grid after backtracking
                    return False  # No valid number found
        return True  # Solved


def printBoard(grid):
        strGrid = ''
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    strGrid += f'| \033[30m{grid[i][j]}\033[30m '
                else:
                    strGrid += '| \033[31m0\033[30m '
                if j == 8:
                    strGrid += '\033[30m|\033[30m'
            if i != 8:
                strGrid += '\n'
        os.system('cls')
        return strGrid
    

# Example Sudoku board
sudoku_api = SudokuAPI(difficulty="hard")
board1 = sudoku_api.fetch_board()
board = board1
solver = SudokuSolver(board)

if solver.solve():
    print("Solved Sudoku:")
    print(solver, solver.counter)
    print(board.__repr__, board1.__repr__)
else:
    print("No solution exists.")

