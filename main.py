import numpy as np
board = np.array([[' ',' ',' '],
                 [' ',' ',' '],
                 [' ',' ',' ']])
count = -1
def show_board():
    """Print the board in the shape of board."""
    global count
    count += 1
    for i in range(3):
        print("_|_".join(board[i]))

def check_winner(board) -> bool:
    """Return True if any player wins the game."""
    winner = False
    # Start checking after 4 moves.
    if count < 5:
        return winner
    for i in range(3):
        row = board[i, :]
        if len(set(row)) == 1:
            winner = True
        col = board[:, i]
        if len(set(col)) == 1:
            winner = True
    digonal = [str(board[j][j]) for j in range(3)]
    anti_diognal = [str(board[j][2-j]) for j in range(3)]
    if len(set(digonal)) == 1 or len(set(anti_diognal)) == 1:
        winner = True
    return winner

show_board()     
while(count < 9):
    # Check which player move it is.
    sign = 'X' if count % 2 == 0 else 'O'
    user_choice = input(f"Player {sign}! Enter your Turn (row column): ")
    try:
        # Convert the entered data in a useable form.    
        user_choice = user_choice.split()
        loc = [int(num)-1 for num in user_choice]

        if loc[0] > 2 or loc[1] > 2:
            print('Please Enter a valid box Number.')
            continue
    except:
        print("Please enter your choice in given form (row col)")
        continue
    else:
        if board[loc[0]][loc[1]] != " ":
            print("The box is already taken try a different box instead.")
            continue
        board[loc[0], loc[1]] = 'X' if count % 2 == 0 else 'O'
        show_board()
        result = check_winner(board=board)
        if result:
            print(f"Player {sign} won the match. Congratulations!")
            break
        # check if game is over.
        if count == 9:
            print("It's a draw. Play again to reach any decision.")
