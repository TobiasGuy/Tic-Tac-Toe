# Import libraries if necessary:
import random
import sys
from time import sleep

# Variables to initialise:
gamemode = "0" # Use 0, 1, 2 for main menu, single player, multi-player respectively
player_turn = 1
board = []

def main():
    # Randomize the starting turn
    player_turn = random.randint(1, 2)
    gamemode = "0"
    for _ in range(0, 9):
        board.append(" ")

    while True: # Entire game active loop

        # Prompt user to choose between single player (vs ai), or 2 player, or let them exit
        # Validate input, make sure it's good, if not then reprompt
            # Should be pretty simple
            # Type 1 for single, 2 for multi, q for quit?
            # Check that user input matches one of the inputs you want
        while True: # Choose gamemode loop
            try:
                gamemode = input("Enter 1 for single player, 2 for multi player, or q to quit ").strip()
            except EOFError:
                sys.exit("File exited")
            if gamemode == "q":
                sys.exit("Quitting game...")
            elif gamemode == "1":
                break
            elif gamemode == "2":
                break
            else:
                print("Invalid input")
                continue
        
        while True: # Current game loop
            # Prompt user for input for choosing position
            # Validate input, make sure it's good, if not then reprompt
                # Input position between 1-9 (maybe coordinates didn't decide yet)
                # Check that the square doesn't already have an X or O in it!
            while True: # Choose position loop
                if player_turn == 1:
                    print("Player 1 / X's turn to move")
                else:
                    print("Player 2 / O's turn to move")
                try:
                    choice = input("Choose a position from 1-9: ").strip()
                    choice = int(choice)
                except ValueError:
                    print("Must input a number")
                    continue
                except EOFError:
                    sys.exit("File exited")
                # Check number is in range
                if choice > 9 or choice < 1:
                    print("Number out of range")
                    continue
                # Check if space is already taken
                if board[choice - 1] == "X" or board[choice - 1] == "O":
                    print("Space already taken")
                    continue
                # Add the choice to the board
                if player_turn == 1:
                    board[choice - 1] = "X"
                    break
                elif player_turn == 2:
                    board[choice - 1] = "O"
                    break
                else:
                    sys.exit("Player turn out of bounds. Something went wrong")
                
            player_turn = switch_turn(player_turn)
            display_board(board)
            result = check_board(board)
            if result == "Player 1 wins!" or result == "Player 2 wins!" or result == "Draw!":
                break

        print("Game over! " + result)
        sleep(2)
        print("---------NEW GAME---------")
    


def display_board(board):
    # Display 'board' that you're playing on
        # Probably make a function for this
        # Display after prompt, before win/loss, and reprompt if the game is not over
        # Do this with coordinates? or 1-9? Maybe for bigger scale coordinates would be good but might not be necessary for this
        # Choose between 1 array vs multi-dimensional array to store values
            # I'll use a 2d array think that might make things nicer -- nvm
    # |---|---|---|                         |---|---|---|
    # |   |   |   |                         |   |   |   |
    # | X | O | X |                         |[0]|[1]|[2]|
    # |   |   |   |                         |   |   |   |
    # |---|---|---|                         |---|---|---|
    # |   |   |   |                         |   |   |   |
    # | X | O | X |                         |[3]|[4]|[5]|
    # |   |   |   |                         |   |   |   |
    # |---|---|---|                         |---|---|---|
    # |   |   |   |                         |   |   |   |
    # | X | O | X |                         |[6]|[7]|[8]|
    # |   |   |   |                         |   |   |   |
    # |---|---|---|                         |---|---|---|
    empty_line = "|   |   |   |"
    filled_line = "|---|---|---|"
    line_one = "| " + board[0] + " | " + board[1] + " | " + board[2] + " |"
    line_two = "| " + board[3] + " | " + board[4] + " | " + board[5] + " |"
    line_three = "| " + board[6] + " | " + board[7] + " | " + board[8] + " |"

    print(filled_line)
    print(empty_line)
    print(line_one)
    print(empty_line)
    print(filled_line)
    print(empty_line)
    print(line_two)
    print(empty_line)
    print(filled_line)
    print(empty_line)
    print(line_three)
    print(empty_line)
    print(filled_line)

    return

def ai_move():
    # Create ai enemy 
        # Only active when it's single player
        # Probably make a variable that changes when you want it to be active or not.
        # Remember to reset this value on new game -- maybe make a list of values to reset?
        # Make sure ai actually moves on its turn
    return

def board_update(): # Might not need this
    # Update 'board' with new inputs and display
        # Store X or O depending on player's turn
        # Randomise on game start? Also display who's turn it currently is
    return

def check_board(board):

    # Check for 3 in a row
    # Check rows: 
    if board[0] == board[1] == board[2] == "X":
        return("Player 1 wins!")
    elif board[0] == board[1] == board[2] == "O":
        return("Player 2 wins!")
    elif board[3] == board[4] == board[5] == "X":
        return("Player 1 wins!")
    elif board[3] == board[4] == board[5] == "O":
        return("Player 2 wins!")
    elif board[6] == board[7] == board[8] == "X":
        return("Player 1 wins!")
    elif board[6] == board[7] == board[8] == "O":
        return("Player 2 wins!")
    
    # Check columns:
    if board[0] == board[3] == board[6] == "X":
        return("Player 1 wins!")
    elif board[0] == board[3] == board[6] == "O":
        return("Player 2 wins!")
    elif board[1] == board[4] == board[7] == "X":
        return("Player 1 wins!")
    elif board[1] == board[4] == board[7] == "O":
        return("Player 2 wins!")
    elif board[2] == board[5] == board[8] == "X":
        return("Player 1 wins!")
    elif board[2] == board[5] == board[8] == "O":
        return("Player 2 wins!")

    # Check diagonals:
    if board[0] == board[4] == board[8] == "X":
        return("Player 1 wins!")
    elif board[0] == board[4] == board[8] == "O":
        return("Player 2 wins!")
    elif board[2] == board[4] == board[6] == "X":
        return("Player 1 wins!")
    elif board[2] == board[4] == board[6] == "O":
        return("Player 2 wins!")

        # return("Player 1 wins!")
        # return("Player 2 wins!")
    
    # Check for whole board being full
        # Loop through each position and if they're all full, call a draw
    if " " not in board:
        return("Draw!")
    
    return("No winner found yet")

def switch_turn(turn):
    # Keep track of who's turn it is, X and O respectively
        # Have a variable that switches after each turn is taken
    if turn == 1:
        return 2
    elif turn == 2:
        return 1

def game_end():
    # After game is done, print winner, prompt user asking if they want to play again or exit
        # Maybe a big while true loop only for this reason that breaks if you want to exit and continues otherwise?
    return


if __name__ == "__main__":
    main()

# Features for later:
    # Leaving these things alone for now
# Later add a scoreboard?
# Username?
# Add an option to access the scoreboard when selecting single or multi-player
# Add a proper UI instead of just using the terminal?
