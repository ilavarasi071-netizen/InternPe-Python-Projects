import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SPEED = 100
SPACE = 20

snake = [(100,100),(80,100),(60,100)]
direction = "Right"
food = (0,0)
score = 0

def create_food():
    global food
    x = random.randint(0,(WIDTH//SPACE)-1)*SPACE
    y = random.randint(0,(HEIGHT//SPACE)-1)*SPACE
    food = (x,y)
    canvas.create_oval(x,y,x+SPACE,y+SPACE,fill="red",tag="food")

def move():
    global snake, score

    x,y = snake[0]
    if direction=="Up": y-=SPACE
    if direction=="Down": y+=SPACE
    if direction=="Left": x-=SPACE
    if direction=="Right": x+=SPACE

    new_head = (x,y)
    snake.insert(0,new_head)

    if new_head == food:
        score+=1
        canvas.delete("food")
        create_food()
    else:
        snake.pop()

    if x<0 or x>=WIDTH or y<0 or y>=HEIGHT or new_head in snake[1:]:
        canvas.create_text(200,200,text="Game Over",
                           fill="white",font=("Arial",30))
        return

    canvas.delete("snake")
    for part in snake:
        canvas.create_rectangle(part[0],part[1],
                                part[0]+SPACE,part[1]+SPACE,
                                fill="green",tag="snake")

    root.after(SPEED,move)

def change_dir(new_dir):
    global direction
    direction=new_dir

root=tk.Tk()
root.title("Snake Game")

canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()

create_food()
move()

root.bind("<Up>",lambda e:change_dir("Up"))
root.bind("<Down>",lambda e:change_dir("Down"))
root.bind("<Left>",lambda e:change_dir("Left"))
root.bind("<Right>",lambda e:change_dir("Right"))

root.mainloop()
