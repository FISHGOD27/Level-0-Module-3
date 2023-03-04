import random
import turtle
from tkinter import simpledialog, messagebox


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    turt = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)ok

    #      3) Set the pen width to 10
    turt.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
    lar=simpledialog.askstring(title="yeet", prompt="what color would you like")
    #      5) Use an if/else statement to set the pen color that the user
    if lar=="red":
        turt.color("red")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar=="blue":
        turt.color("blue")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar=="green":
        turt.color("green")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar =="purple":
        turt.color("purple")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar =="yellow":
        turt.color("yellow")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar =="teal":
        turt.color("#737373")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar =="black":
        messagebox.showinfo(message="Out of all the colors you chose black? Why not green or blue? Ok fine")
        turt.color("black")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    elif lar =="white":
        messagebox.showinfo(message="Out of all the colors you chose white? Why not green or blue? Ok fine")
        window.bgcolor("black")
        turt.color("white")
        turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100), turt.left(90), turt.forward(100)
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
