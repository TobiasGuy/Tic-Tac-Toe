# Import libraries if necessary:
import random
import sys

# Variables to initialise:
gamemode = "0" # Use 0, 1, 2 for main menu, single player, multi-player respectively
player_turn = 1

def main():
    # Randomize the starting turn
    player_turn = random.randint(1, 2)
    gamemode = "0"
    board = []
    # Prompt user to choose between single player (vs ai), or 2 player, or let them exit
    # Validate input, make sure it's good, if not then reprompt
        # Should be pretty simple
        # Type 1 for single, 2 for multi, q for quit?
        # Check that user input matches one of the inputs you want
    while True:
        try:
            gamemode = input("Enter 1 for single player, 2 for multi player, or q to quit").strip()
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
    
    # Prompt user for input for choosing position
    # Validate input, make sure it's good, if not then reprompt
        # Input position between 1-9 (maybe coordinates didn't decide yet)
        # Check that the square doesn't already have an X or O in it!
    while True:
        try:
            choice = input("Choose a position from 1-9:").strip()
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
        if board[choice] == "X" or board[choice] == "O":
            print("Space already taken")
            continue
        # Add the choice to the board
        if player_turn == 1:
            board[choice] = "X"
            player_turn = 2
            break
        elif player_turn == 2:
            board[choice] = "O"
            player_turn = 1
            break
        else:
            sys.exit("Something went wrong")


    
    return

def display_board():
    # Display 'board' that you're playing on
        # Probably make a function for this
        # Display after prompt, before win/loss, and reprompt if the game is not over
        # Do this with coordinates? or 1-9? Maybe for bigger scale coordinates would be good but might not be necessary for this
        # Choose between 1 array vs multi-dimensional array to store values
            # I'll use a 2d array think that might make things nicer
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

def check_board():
    # Check for 3 in a row
        # Probably a function for checking each direction: Vertical, Horizontal, Diagonal
    # Check for whole board being full
        # Loop through each position and if they're all full, call a draw
    return

def switch_turn():
    # Keep track of who's turn it is, X and O respectively
        # Have a variable that switches after each turn is taken
    return

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
