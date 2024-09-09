# Tic-Tac-Toe Game

## Overview

This repository contains an advanced Python implementation of the Tic-Tac-Toe game, featuring both single-player mode (against a basic AI) and two-player mode. The game uses a command-line interface to interact with players, providing a straightforward way to play Tic-Tac-Toe and enhancing the experience with basic AI functionality.

## Features

- **Game Modes**:
  - **Single-Player**: Compete against a simple AI that makes random moves.
  - **Two-Player**: Play with another person on the same device.
- **Interactive CLI**: Uses a command-line interface to display the game board and prompt for user input.
- **Input Validation**: Ensures valid moves and provides error messages for invalid inputs.
- **Board Display**: Displays the game board in a 3x3 grid format.
- **Replay Functionality**: Allows players to start a new game after the current game ends.

## Game Instructions

1. **Run the Game**:
   Execute the script in your Python environment with the command:
   ```bash
   python tic_tac_toe.py
   ```

2. **Choose Game Mode**:
   - Input `1` for single-player mode (against AI).
   - Input `2` for two-player mode.

3. **Make a Move**:
   - Players choose a move by entering a number from `1-9`, corresponding to the board positions:
     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```
   - The board is updated after each move.

4. **Winning Condition**:
   - Align three of your marks horizontally, vertically, or diagonally to win.
   - If the board is full and no player has won, the game results in a tie.

5. **End of Game**:
   - After a win or tie, the board is displayed, and players are asked if they want to play again.
   - Input `y` to play again or `n` to exit.

## Code Structure

- **`print_board(board)`**: Prints the current state of the game board in a readable format.
- **`check_winner(board, player)`**: Determines if the current player has won by checking rows, columns, and diagonals.
- **`is_full(board)`**: Checks if the board is completely filled with no empty spots.
- **`get_valid_input(board)`**: Prompts the user for a move and ensures it's a valid, unoccupied spot.
- **`ai_move(board, player)`**: Selects a random move for the AI in single-player mode.
- **`tic_tac_toe()`**: The main game loop that manages the game's flow and player turns.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShreyasGowda28/tic-tac-toe.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd tic-tac-toe
   ```
3. **Ensure Python 3 is Installed**:
   This script requires Python 3.x.

4. **Run the Script**:
   ```bash
   python tic_tac_toe.py
   ```

## Example Gameplay

```
Enter game mode: 1
Player X's turn.
Enter your move (1-9): 5
  |   |  
---------
  | X |  
---------
  |   |  

AI's turn.
  |   |  
---------
  | X | O
---------
  |   |  

Player X wins!
```

## Future Enhancements

- **AI Improvements**: Implement a more strategic AI using algorithms like Minimax for better gameplay.
- **GUI Integration**: Develop a graphical user interface using libraries like Tkinter or Pygame.
- **Difficulty Levels**: Introduce different AI difficulty levels to challenge players of all skill levels.
- **Enhanced Input Handling**: Improve the input system to handle more complex scenarios and provide better user feedback.

## License

This project is open-source and free for personal or educational use. For commercial use, please contact the author.