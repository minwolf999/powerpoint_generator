from tkinter import *
from tkinter import filedialog

# The Image class handle an image element of a page
class Image:
    # We define:
        # - a tkinter Frame where all the elements will be implemented
        # - a name
        # - the path of an image
        # - the space left to the left of the image
        # - the space left to the top of the image
        # - the width of the image
        # - the height of the image
    def __init__(self, tk, i):
        self.tk = tk
        self.name = f"Image{i}"
        self.path = ""
        self.left = 0.0
        self.top = 0.0
        self.width = 0.0
        self.height = 0.0


    # The AddImage method gonna implement the elements in the tkinter frame
    def AddImage(self):
        # We add a text who say we are on a new image element
        Label(self.tk, text="Add a new image", font="bold").pack(anchor='e', pady=(25,3))

        # We add a button to select en image
        Label(self.tk, text="Select an image").pack(anchor='e', pady=3)
        self.in_image = Button(self.tk, text="Choose your image", command=self.SetImage)
        self.in_image.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the space left to the left of the image
        leftTemp = StringVar()
        leftTemp.trace_add("write", lambda name, index, mode, sv=leftTemp: self.SetLeft(sv))
        Label(self.tk, text="Place to the left of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_left = Entry(self.tk, textvariable=leftTemp)
        self.in_left.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the space left to the top of the image
        topTemp = StringVar()
        topTemp.trace_add("write", lambda name, index, mode, sv=topTemp: self.SetTop(sv))
        Label(self.tk, text="Place to the top of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_top = Entry(self.tk, textvariable=topTemp)
        self.in_top.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the width of the image
        widthTemp = StringVar()
        widthTemp.trace_add("write", lambda name, index, mode, sv=widthTemp: self.SetWidth(sv))
        Label(self.tk, text="Width of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_width = Entry(self.tk, textvariable=widthTemp)
        self.in_width.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the height of the image
        heightTemp = StringVar()
        heightTemp.trace_add("write", lambda name, index, mode, sv=heightTemp: self.SetHeight(sv))
        Label(self.tk, text="Height of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_height = Entry(self.tk, textvariable=heightTemp)
        self.in_height.pack(anchor='e', pady=3)


    # This method gonna open the choose file popup
    def SetImage(self):
        self.path = filedialog.askopenfilename()


    # This method gonna set the number enter for the left class variable
    def SetLeft(self, sv):
        try:
            # If the texte is empty we set 0.0
            if (sv.get() == ""):
                self.top = 0.0
            # If the text is a valid number we convert it in float and store it
            else:
                self.top = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_left.delete(0, 'end')


    # This method gonna set the number enter for the top class variable
    def SetTop(self, sv):
        try:
            # If the texte is empty we set 0.0
            if (sv.get() == ""):
                self.top = 0.0
            # If the text is a valid number we convert it in float and store it
            else:
                self.top = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_top.delete(0, 'end')


    # This method gonna set the number enter for the width class variable
    def SetWidth(self, sv):
        try:
            # If the texte is empty we set None
            if (sv.get() == ""):
                self.width = 0.0
            # If the text is a valid number we convert it in float and store it
            else:
                self.width = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_width.delete(0, 'end')


    # This method gonna set the number enter for the height class variable
    def SetHeight(self, sv):
        try:
            # If the texte is empty we set None
            if (sv.get() == ""):
                self.height = 0.0
            # If the text is a valid number we convert it in float and store it
            else:
                self.height = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_height.delete(0, 'end')
