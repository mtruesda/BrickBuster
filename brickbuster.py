# 
# Author: Myron Truesdale
# @@Version 06/27/22
# BrickBuster
#

# imports
from tkinter import *
from tkinter import ttk

# use object to run the GUI
class game():
    def __init__(self):
        # initialize the window 
        self.root = Tk()
        self.root.geometry = ("1400x1200")
        self.root.title("Brickbuster")

        mainPage()

    def mainPage(self):
        self.mainLabel = ttk.Label(self.root, text='BrickBuster', font=("Calibri,26"), padding="10px")
        

game()

