from tkinter import *
from tkinter import colorchooser

from models.textClass import Text
from models.imageClass import Image

# The Page class handle a page of the powerpoint
class Page:
    # We define:
        # - a tkinter Frame where all the elements will be implemented
        # - a name
        # - a start (which will be the hexadecimal of a color) 
        # - an end (which will be the hexadecimal of a color)
        # - a list of children
    def __init__(self, tk, i):
        self.tk = tk
        self.name = f"Diap{i}"
        self.start = "000000"
        self.end = "000000"
        self.children = []


    # The AddPage method gonna implement the elements in the tkinter frame
    def AddPage(self):
        # We add a text who say we are on a new page
        Label(self.tk, text="Add a new layout to the powerpoint", font="bold").pack(anchor='e', pady=(25,3))

        # We add some text and a button to select a color for the top of the page
        Label(self.tk, text="Background Color at the top of the Layout").pack(anchor='center', pady=3)
        self.bg_top = Button(self.tk, text="Pick a color", command=self.SetEnd)
        self.bg_top.pack(anchor='center', pady=3)

        # We add some text and a button to select a color for the bottom of the page
        Label(self.tk, text="Background Color at the bottom of the Layout").pack(anchor='center', pady=3)
        self.bg_bottom = Button(self.tk, text="Pic a color", command=self.SetStart)
        self.bg_bottom.pack(anchor='center', pady=3)

        # We add 2 buttons one to add text in the page, and the other to add an image
        Button(self.tk, text="Add text", command=self.CreateText).pack(anchor='center', pady=(25, 3))
        Button(self.tk, text="Add image", command=self.CreateImage).pack(anchor='center', pady=3)


    # This method will set the chosen color in the class variable start
    def SetStart(self):
        # We open a color form and store the color chosen
        color_code = colorchooser.askcolor(title="Choose Background Top Color")[1]
        if color_code:
            self.bg_bottom.config(bg=color_code)
            self.start = color_code[1:]


    # This method will set the chosen color in the class variable end
    def SetEnd(self):
        # We open a color form and store the color chosen
        color_code = colorchooser.askcolor(title="Choose Background Top Color")[1]
        if color_code:
            self.bg_top.config(bg=color_code)
            self.end = color_code[1:]


    # This method create a new Text instance a store them in the children list  
    def CreateText(self):
        text = Text(self.tk, len(self.children))
        text.AddText()
        self.children.append(text)


    # This method create a new Image instance a store them in the children list
    def CreateImage(self):
        image = Image(self.tk, len(self.children))
        image.AddImage()
        self.children.append(image)