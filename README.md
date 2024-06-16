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