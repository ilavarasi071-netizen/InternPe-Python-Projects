import tkinter as tk
from tkinter import messagebox

# Initialize board and player
board = [""] * 9
current_player = "X"

def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return True
    return False

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 30),
                       width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = tk.Button(root, text="Reset", font=("Arial", 15),
                         command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
