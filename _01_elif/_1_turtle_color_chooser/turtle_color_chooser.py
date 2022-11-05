import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    jimmy = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    count = 0
    while(count == 0):
        for i in range(4):
            jimmy.forward(100)
            jimmy.right(90)
    #      3) Set the pen width to 10
        jimmy.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
        a = simpledialog.askstring("Color", "What color pen would you like to draw with?")
        #      5) Use an if/else statement to set the pen color that the user
        #         requested
        if(a == "green"):
            jimmy.pencolor("green")
        elif(a == "red"):
            jimmy.pencolor("red")
        elif(a == "orange"):
            jimmy.pencolor("orange")
        elif(a == "yellow"):
            jimmy.pencolor("yellow")
        elif(a == "blue"):
            jimmy.pencolor("blue")
        elif(a == "purple"):
            jimmy.pencolor("purple")
        #      6) If the user doesn't enter anything, choose a random color
        elif(a == ""):
            jimmy.pencolor(get_random_color())
        #      7) Put a loop around your code so that you keep asking the user for
        #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
