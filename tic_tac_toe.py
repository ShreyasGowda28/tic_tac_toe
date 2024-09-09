import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([spot != ' ' for row in board for spot in row])

def get_valid_input(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in range(1, 10):
                row, col = divmod(move - 1, 3)
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Spot already taken. Try again.")
            else:
                print("Invalid input. Please enter a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board, player):
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    row, col = random.choice(empty_spots)
    board[row][col] = player

def tic_tac_toe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        players = ['X', 'O']
        current_player = 0

        game_mode = input("Choose game mode: '1' for single-player (vs AI), '2' for two-player: ")

        while True:
            print_board(board)
            if game_mode == '1' and players[current_player] == 'O':
                print("AI's turn.")
                ai_move(board, players[current_player])
            else:
                print(f"Player {players[current_player]}'s turn.")
                row, col = get_valid_input(board)
                board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 1 - current_player

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()
