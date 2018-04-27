#!/usr/bin/env python3

'''
ball.py : illustrate threading with an animation

Copyright (C) Simon D. Levy 2016

Modified by Collin Sherman

Adapted from  http://stackoverflow.com/questions/25430786/moving-balls-in-tkinter-canvas
'''
from tkinter import *
from threading import Thread
from time import sleep, time

class Ball:

    def __init__(self, canvas, x, y, r):

        self.canvas = canvas
        self.oval = canvas.create_oval(x, y, x+2*r, y+2*r, fill="red")

        self.x = 0          # stores current horizontal position
        self.direction = +1 # start by moving rightward
        self.quit = False   # flag for user wanting to quit

    def animate(self):

        # If user wanted to quit, we're done
        if self.quit:
            exit(0)

        # Arbitrary horzontal step size
        DX = 5

        # Increment or decrement the ball's position
        self.x += self.direction * DX


        w = self.canvas.winfo_width()

        # If ball has gone to the right edge of the canvas, reset it to the leftO
        if self.direction == +1:
            if self.x > w:
                self.x = 0
                dx = -w # A giant step leftward

            # Otherwise, keep moving rightward
            else:
                dx = +DX

        else:
            if self.x <= 0:
                self.x = w
                dx = w # A giant step rightward

            # Otherwise, keep moving leftward
            else:
                dx = -DX

        self.canvas.move(self.oval, dx, 0)
        
        self.canvas.after(50, self.animate) # recursive call after 50 milliseconds

    def setDirection(self, direction):
        """Changes direction that ball moves"""
        
        if direction == "right" or direction == "r":
            self.direction = +1
            return
        elif direction == "left" or direction == "l":
            self.direction = -1
            return
        else:
            print("Invalid command.")
            return


def updater(ball):
    """Takes inuput from user and changes the movement of the ball in the GUI, or quits the program."""

    while True:

        command = input("Would you like to go left, right, or quit? ")
        command = command.lower()

        if command == "quit" or command == "q":
            ball.quit = True
            break
        else:
            ball.setDirection(command)

if __name__ == '__main__':

    CANVAS_SIZE = 300

    # initialize root Window and canvas
    root = Tk()
    root.title("Ball")
    root.resizable(False,False)
    canvas = Canvas(root, width = CANVAS_SIZE, height = CANVAS_SIZE)
    canvas.pack()

    # create a ball object at middle-left in the display and animate it
    ball = Ball(canvas, 0, CANVAS_SIZE/2, 10)

    # run thread for user input, passing ball object to thread's method
    thread = Thread(target=updater, args=(ball,))
    thread.daemon = True
    thread.start()

    # animate the ball
    ball.animate()
    root.mainloop()
