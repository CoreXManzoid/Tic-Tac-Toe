import numpy as np
import tkinter as tk
from tkinter import messagebox
from functools import partial # Alows us to call parameterize function inside a function.

# set our window screen.
window = tk.Tk()
window.title('Tic Tac Toe')

"""Initilize empty DATA"""
count = 0
# Generate a 2D 3*3 Array with spaces as element.
board = np.array([[' ' for _ in range(3)] for _ in range(3)])
Button = [[None for _ in range(3)] for _ in range(3)]

def check_winner(board) -> list:
    """Return a list of result and boxes if any player wins the game."""
    winner = [False]
    for i in range(3):
        row = board[i, :]
        if len(set(row)) == 1 and row[0] != " ":
            winner = [True, [i,0], [i,1], [i, 2]]
        col = board[:, i]
        if len(set(col)) == 1 and col[0] != " ":
            winner = [True ,[0,i],[1,i],[2,i]]
    digonal = [str(board[j][j]) for j in range(3)]
    anti_diognal = [str(board[j][2-j]) for j in range(3)]
    if len(set(digonal)) == 1 and digonal[0] != " ":
        winner = [True, [0,0], [1,1], [2,2]]
    elif len(set(anti_diognal)) == 1 and anti_diognal[0] != " ":
        winner = [True, [0,2], [1,1], [2,0]]

    return winner

def button_click(r, c):
    global count
    # Check which player move it is.
    sign = 'X' if count % 2 == 0 else 'O'
    color = 'crimson' if sign == 'X' else 'orange'
    # Update our data
    if board[r][c] == " ":
        board[r][c] = sign
        Button[r][c].config(text = sign, fg=color)
        count += 1
        result = check_winner(board=board)
        # check if any winner and follow corresponding code
        if result[0] or count == 9:
            if result[0]:
                for res in result[1:]:
                    Button[res[0]][res[1]].config(bg='green')
                option = messagebox.askyesno(title="Game Over", message=f"Player {sign} won the match. Congratulations!\nWanna Play Again!")
                # check if game is over.
            else:
                option = messagebox.askyesno(title="Game Over",message="It's a draw. Wanna Play Again!")
            # Ask the user if he want to play again. if yes then reset our data.
            if option:
                count = 0
                for r in range(3):
                    for c in range(3):
                        Button[r][c].config(text=" ", bg='white')
                        board[r][c] = " "
    else:
        messagebox.showwarning(title='Wrong Turn', message="Please chose another box.")

#-------------------- GUI SetUp -----------------------------# 
for r in range(3):
    for c in range(3):
        button = tk.Button(text=' ', font=('Arial', 28, 'bold'), width=4, height=2, command=partial(button_click, r, c))
        button.grid(row=r, column=c)
        Button[r][c] = button
        

window.mainloop()