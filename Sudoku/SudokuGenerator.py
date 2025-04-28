import requests

class SudokuAPI:
    def __init__(self, difficulty="hard"):
        self.base_url = "https://sugoku.onrender.com/board"
        self.difficulty = difficulty

    def fetch_board(self):
        try:
            response = requests.get(self.base_url, params={"difficulty": self.difficulty})
            response.raise_for_status()
            data = response.json()
            return data["board"]
        except Exception as e:
            print(f"Error fetching Sudoku board: {e}")
            return None

    def display_board(self, board):
        for row in board:
            print(row)

if __name__ == "__main__":
    sudoku_api = SudokuAPI(difficulty="hard")  # Change difficulty to "easy", "medium", or "hard" as needed
    board = sudoku_api.fetch_board()
    if board:
        print("Generated Sudoku Board:")
        sudoku_api.display_board(board)
