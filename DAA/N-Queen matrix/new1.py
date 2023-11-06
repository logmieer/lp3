class NQueens:
    def __init__(self, size):
        self.size = size
        # Initialize the chessboard as a 2D array of False (no queens placed)
        self.board = [[False] * size for _ in range(size)]
        self.count = 0  # Initialize the count of solutions found

    def printBoard(self):
        # Print the chessboard with 'Q' indicating queens and 'X' indicating empty squares
        for row in self.board:
            for ele in row:
                if ele == True:
                    print("Q", end=" ")
                else:
                    print("X", end=" ")
            print()
        print()

    def isSafe(self, row, col):
        # Check if it's safe to place a queen at a given row and column

        # Check Column(above and below of the (row, col))
        for i in range(self.size):
            if self.board[i][col] == True:
                return False

        # Check backward slash(\) diagonal only in above direction
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == True:
                return False
            i -= 1
            j -= 1
        # Check backward slash(\) diagonal only in below direction
        i = row
        j = col
        while i < self.size and j < self.size:
            if self.board[i][j] == True:
                return False
            i += 1
            j += 1

        # Check forward slash diagonal(/) only in above direction
        i = row
        j = col
        while i >= 0 and j < self.size:
            if self.board[i][j] == True:
                return False
            i -= 1
            j += 1

        # Check forward slash diagonal(/) only in below direction
        i = row
        j = col
        while i < self.size and j >= 0:
            if self.board[i][j] == True:
                return False
            i += 1
            j -= 1

        return True

    def set_position_first_queen(self, row, col):
        # Set the position of the first queen based on user input
        self.board[row - 1][col - 1] = True
        self.printBoard()

    def solve(self, row):
        # Solve the N-Queens problem using backtracking

        if row == self.size:
            # If all queens are placed, print the board and increment the count of solutions
            self.count += 1
            self.printBoard()
            return

        if any(self.board[row]) is True:
            # If any queen is already placed in the current row, move to the next row
            self.solve(row + 1)
            return

        for col in range(self.size):
            if self.isSafe(row, col) == True:
                # If it's safe to place a queen at the current row and column, place the queen
                self.board[row][col] = True
                self.solve(row + 1)  # Recursively move to the next row
                # Backtrack to explore other possibilities
                self.board[row][col] = False

    def displayMessage(self):
        if self.count > 0:
            print("Solution exists for the given position of the queen.")
        else:
            print("Solution doesn't exist for the given position of the queen.")


# Example usage for an 8x8 board
size = 8
solver = NQueens(size)
row = int(input(f"Enter row (1-{size}) for the first queen: "))
col = int(input(f"Enter column (1-{size}) for the first queen: "))
solver.set_position_first_queen(row, col)
solver.solve(0)
solver.displayMessage()
