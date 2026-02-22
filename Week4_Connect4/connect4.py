import tkinter as tk
from tkinter import messagebox

r, c = 6, 7
turn = ['red']

def drop(event):
    x = event.x // 70
    for y in range(r-1, -1, -1):
        if not board[y][x]:
            board[y][x] = turn[0]
            canvas.itemconfig(cells[y][x], fill=turn[0])
            if win(y, x):
                messagebox.showinfo("Game Over", f"{turn[0].capitalize()} Wins!")
                reset()
            turn[0] = 'yellow' if turn[0] == 'red' else 'red'
            break

def win(y, x):
    def cnt(dx, dy):
        i = j = 1
        while 0 <= y+i*dy < r and 0 <= x+i*dx < c and board[y+i*dy][x+i*dx] == turn[0]: i += 1
        while 0 <= y-j*dy < r and 0 <= x-j*dx < c and board[y-j*dy][x-j*dx] == turn[0]: j += 1
        return i + j - 1 >= 4
    return any(cnt(a, b) for a, b in [(1, 0), (0, 1), (1, 1), (1, -1)])

def reset():
    for y in range(r):
        for x in range(c):
            board[y][x] = None
            canvas.itemconfig(cells[y][x], fill='white')

root = tk.Tk()
root.title("Connect 4")

canvas = tk.Canvas(root, width=c*70, height=r*70, bg='blue')
canvas.pack()

board = [[None]*c for _ in range(r)]
cells = [[canvas.create_oval(x*70+5, y*70+5, x*70+65, y*70+65, fill='white')
          for x in range(c)] for y in range(r)]

canvas.bind("<Button-1>", drop)

tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()
