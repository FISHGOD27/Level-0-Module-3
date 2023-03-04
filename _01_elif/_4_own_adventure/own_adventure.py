from tkinter import simpledialog, messagebox, Tk

def setup():
    size(500, 500)
    global x
    global y
    x = 250
    y = 250
    fill("#0343FC")
    textSize(10)
    text("press left to go left, right to go right, down to stop moving", width/2, height/2)
def draw():
    background(200, 200, 200)
    global x
    global y
    ellipse(x, y, 50, 50)
    if keyCode == RIGHT:
        x+=5
    elif keyCode == LEFT:
        x-=5



