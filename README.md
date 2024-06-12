# Tic-Tac-Toe
 Basic python tic-tac-toe recreation

#### 2024-06-11
# 1
Initial commit done, repo made
TODO: create initial plan (done)

# 2
Finalised initial plan
Copied plan into new file plan.md so it doesn't get lost and can be referenced later when the code gets messier

# 3
Reorganised comments in game.py to put sections in order
Created functions that I might need for each section

#### 2024-06-12
# 1 Gamemode Selection
Coded the gamemode selection input section and validation

# 2 Position Selection
Coded the position selection input section
Validation:
    Check if input is an integer
    Check if input is within range of board
    Check if location on board is already taken
Note: thinking I might not need board_update() function at this point, will keep the definition for now but not add anything in it
Small fix: Added .strip() to gamemode selection input