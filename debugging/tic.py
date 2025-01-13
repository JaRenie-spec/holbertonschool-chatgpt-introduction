def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Parameters:
    board (list of lists): The tic-tac-toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Checks if the board is full (no empty spaces left).

    Parameters:
    board (list of lists): The tic-tac-toe board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the tic-tac-toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate row and column input
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 0 and 2. Try again.")
                continue

            # Check if the spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place the player's marker
            board[row][col] = player

            # Check if the current player has won
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check if the board is full
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input! Please enter numbers only. Try again.")
        except IndexError:
            print("Invalid input! Row and column must be between 0 and 2. Try again.")

# Start the game
tic_tac_toe()
