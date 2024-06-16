# TODO

## Create ai enemy 
    # Only active when it's single player
    # Probably make a variable that changes when you want it to be active or not.
    # Remember to reset this value on new game -- maybe make a list of values to reset?

## Check for 3 in a row
    # Probably a function for checking each direction: Vertical, Horizontal, Diagonal

## Check for whole board being full
    # Loop through each position and if they're all full, call a draw

## After game is done, print winner, prompt user asking if they want to play again or exit
    # Maybe a big while true loop only for this reason that breaks if you want to exit and continues otherwise?

## Clean up code / main function
    # Split more things into functions to make main function more readable



# TEST PHASE

## Display 'board' that you're playing on
    # Probably make a function for this
    # Display after prompt, before win/loss, and reprompt if the game is not over

## Store 'board' values

## Prompt user to choose between single player (vs ai), or 2 player
## Validate input, make sure it's good, if not then reprompt
    # Should be pretty simple
    # Type 1 for single, 2 for multi
    # Check that user input matches one of the inputs you want

## Prompt user for input for choosing position
## Validate input, make sure it's good, if not then reprompt
    # Input position between 1-9 (maybe coordinates didn't decide yet)
    # Check that the square doesn't already have an X or O in it!

## Keep track of who's turn it is, X and O respectively
    # Have a variable that switches after each turn is taken

## Update 'board' with new inputs and display
    # Store X or O depending on player's turn
    # Randomise on game start? Also display who's turn it currently is




# COMPLETED + TESTED





# Features for later:
    # Leaving these things alone for now
## Later add a scoreboard?
## Username?
## Add an option to access the scoreboard when selecting single or multi-player
## Add a proper UI instead of just using the terminal?
