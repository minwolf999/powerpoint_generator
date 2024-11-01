from tkinter import *
from tkinter import colorchooser

# The Text class handle a text element of a page
class Text:
    # We define:
        # - a tkinter Frame where all the elements will be implemented
        # - a name
        # - the text
        # - the space left to the left of the image
        # - the space left to the top of the image
        # - the width of the image
        # - the height of the image
        # - the font color
        # - the font size
        # - the font family
        # - if font is bold
        # - if font is italic
        # - if font is underline
        # - the align   
    def __init__(self, tk, i):
        self.tk = tk

        self.name = f"Text{i}"

        self.text = ""

        self.left = 0.0
        self.top = 0.0
        self.width = None
        self.height = None

        self.fontcolor = "ffffff"
        self.fontsize = 0
        self.fontname = ""

        self.bold = False
        self.italic = False
        self.underline = False

        self.align = "left"


    # The AddText method gonna implement the elements in the tkinter frame
    def AddText(self):
        # We add a text who say we are on a new text element
        Label(self.tk, text="Add a new text to the layout", font="bold").pack(anchor='e', pady=(25,3))

        # We add a Entry area to enter the text
        textTemp = StringVar()
        textTemp.trace_add("write", lambda name, index, mode, sv=textTemp: self.SetText(sv))
        Label(self.tk, text="Text of your element").pack(anchor='e', pady=3)
        self.in_text = Entry(self.tk, textvariable=textTemp)
        self.in_text.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the space left to the left of the text
        leftTemp = StringVar()
        leftTemp.trace_add("write", lambda name, index, mode, sv=leftTemp: self.SetLeft(sv))
        Label(self.tk, text="Place to the left of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_left = Entry(self.tk, textvariable=leftTemp)
        self.in_left.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the space left to the top of the text
        topTemp = StringVar()
        topTemp.trace_add("write", lambda name, index, mode, sv=topTemp: self.SetTop(sv))
        Label(self.tk, text="Place to the top of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_top = Entry(self.tk, textvariable=topTemp)
        self.in_top.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the width of the text
        widthTemp = StringVar()
        widthTemp.trace_add("write", lambda name, index, mode, sv=widthTemp: self.SetWidth(sv))
        Label(self.tk, text="Width of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_width = Entry(self.tk, textvariable=widthTemp)
        self.in_width.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the height of the text
        heightTemp = StringVar()
        heightTemp.trace_add("write", lambda name, index, mode, sv=heightTemp: self.SetHeight(sv))
        Label(self.tk, text="Height of your element (in Cm)").pack(anchor='e', pady=3)
        self.in_height = Entry(self.tk, textvariable=heightTemp)
        self.in_height.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the font color of the text
        Label(self.tk, text="Font color").pack(anchor='e', pady=3)
        self.in_fontcolor = Button(self.tk, text="Pic a color", command=self.SetFontColor)
        self.in_fontcolor.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the font size of the text
        fontsizeTemp = StringVar()
        fontsizeTemp.trace_add("write", lambda name, index, mode, sv=fontsizeTemp: self.SetFontSize(sv))
        Label(self.tk, text="Font Size").pack(anchor='e', pady=3)
        self.in_fontsize = Entry(self.tk, textvariable=fontsizeTemp)
        self.in_fontsize.pack(anchor='e', pady=3)

        # We add a text and an entry area to define the font family of the text
        fontnameTemp = StringVar()
        fontnameTemp.trace_add("write", lambda name, index, mode, sv=fontnameTemp: self.SetFontName(sv))
        Label(self.tk, text="Font Family").pack(anchor='e', pady=3)
        self.in_fontname = Entry(self.tk, textvariable=fontnameTemp)
        self.in_fontname.pack(anchor='e', pady=3)

        # We add 3 check button to defnie if the font is bold, italic, underline
        Checkbutton(self.tk, text='Bold', command=self.SetBold).pack(anchor='e', pady=3)
        Checkbutton(self.tk, text="Italic", command=self.SetItalic).pack(anchor='e', pady=3)
        Checkbutton(self.tk, text="Underline", command=self.SetUnderline).pack(anchor='e', pady=3)

        # We add a listbox to define the align of the text
        self.in_align = Listbox(self.tk, height=4)
        self.in_align.insert(1, "Left")
        self.in_align.insert(2, "Center")
        self.in_align.insert(3, "Right")
        self.in_align.insert(4, "Justify")
        self.in_align.pack(anchor='e', pady=3)
        self.in_align.bind("<<ListboxSelect>>", self.SetAlign)


    # This method will set the text enter in the text class variable
    def SetText(self, sv):
        self.text = sv.get()
        
    
    # This method will set the number enter for the left class variable
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


    # This method will set the number enter for the top class variable
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


    # This method will set the number enter for the width class variable
    def SetWidth(self, sv):
        try:
            # If the texte is empty we set None
            if (sv.get() == ""):
                self.width = None
            # If the text is a valid number we convert it in float and store it
            else:
                self.width = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_width.delete(0, 'end')


    # This method will set the number enter for the height class variable
    def SetHeight(self, sv):
        try:
            # If the texte is empty we set None
            if (sv.get() == ""):
                self.height = None
            # If the text is a valid number we convert it in float and store it
            else:
                self.height = float(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_height.delete(0, 'end')


    # This method will set the chosen color in the class variable fontcolor
    def SetFontColor(self):
        # We open a color form and store the color chosen
        color_code = colorchooser.askcolor(title="Choose font color")[1]
        if color_code:
            self.in_fontcolor.config(bg=color_code)
            self.fontcolor = color_code[1:]


    # This method will set the number enter for the fontsize class variable
    def SetFontSize(self, sv):
        try:
            # If the texte is empty we set 0
            if (sv.get() == ""):
                self.fontsize = 0
            # If the text is a valid number we convert it in an integer and store it
            else:
                self.fontsize = int(sv.get())
        # If the text isn't a valid number we clear the entry area
        except:
            self.in_fontsize.delete(0, 'end')


    # This method will set the text enter in the fontname class variable
    def SetFontName(self, sv):
        self.fontname = sv.get()


    # This method will set if the font is in bold or not
    def SetBold(self):
        self.bold = not self.bold


    # This method will set if the font is in italic or not
    def SetItalic(self):
        self.italic = not self.italic


    # This method will set if the font is in underline or not
    def SetUnderline(self):
        self.underline = not self.underline


    # This method will set if the align of the font
    def SetAlign(self, e):
        self.align = e.widget.get(int(e.widget.curselection()[0])).lower()
