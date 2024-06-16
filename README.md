# Tic-Tac-Toe
 Basic python tic-tac-toe recreation

### 2024-06-11
#### 1
Initial commit done, repo made
TODO: create initial plan (done)

#### 2
Finalised initial plan
Copied plan into new file plan.md so it doesn't get lost and can be referenced later when the code gets messier

#### 3
Reorganised comments in game.py to put sections in order
Created functions that I might need for each section

### 2024-06-12
#### 1 Gamemode Selection
Coded the gamemode selection input section and validation

#### 2 Position Selection
Coded the position selection input section
Validation:
    Check if input is an integer
    Check if input is within range of board
    Check if location on board is already taken
Note: thinking I might not need board_update() function at this point, will keep the definition for now but not add anything in it
Small fix: Added .strip() to gamemode selection input

#### 3 Small touches
Drew out board display in comments inside display_board() function
Realised I need to adjust the board[choice] to board[choice - 1] because array is 0 index

#### 4 Display Board Function
Coded display_board() function
Also added function calls switch_turn, display_board, check_board.

### 2024-06-16
#### 1 Touch up and small fixes
Display current user's turn
Added spaces after input() functions to make them look cleaner
Imported sleep function. Will use at some point
Fixed bug when clearing the board, trying to access parts of the board list that were not assigned yet. Appended instead of trying to modify

#### 2 Switch turn function, Dsiplay board fix
Fixed switch turn function. Send player_turn as argument and update player_turn to the returned value
Added board as argument to display_board
Changed board creation loop to range(0, 9) because it wasn't long enough
It's alive! The game runs for 1 turn then ends.

#### 3 Keep the game running
Nested most of the main function in a while True loop.
Thinking about separating more things into different functions. Choose gamemode, choose position? Looks pretty ugly with so many nested while True's
Added board as argument to check_board
Added print(filled_line) to the top of the display_board function. Completes the board

#### 4 Fixing plan and backlogging
Self note: Should keep track of how the plan evolves better. Sometimes I do a commit then I'm like: now what do I do? Maybe sign off on some sections as complete, continue updating plan.md?
Making this commit about fixing the plan now
Another self note: I wish I could colour code these sections in the plan. Maybe could make a VSCode extension for this. Or use a different program for taking notes? But it's nice to have this stuff open in VSCode along with my program. Decided to make my headers in ALL CAPS for now
Separated into sections as follows: # TODO, # TEST PHASE, # COMPLETED + TESTED.
Sections are pretty self explanatory. Putting everything in the test phase section until I'm in the finishing touches on the program, this is like a "final check" (code is made, but not signed off on yet)
Fixed plan

#### 5 Made the skeleton for game ending
Preemptively made the return values for check_board when the game is supposed to end but commented them out for now
Made checks accordingly to break out of the while True current game loop
Added the logic to display the winner and start a new game again after 2 seconds

#### 6 Check board function part 1
First check is if the board is full
Decided this was a bad idea because what if someone wins on the last turn (unlikely but possible?)
Moved full board to be the last check instead
Laid out the plan in comments for checking rows, columns, diagonals
Final return means there is no reason to stop the game so it should continue