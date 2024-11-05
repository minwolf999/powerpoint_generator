from tkinter import *

import const
from models.pageClass import Page
from generateJSON.generateJSON import GenerateJSON
from visualizer.Visualizer import Visualizer


# we create a new page for the future powerpoint
def CreatePage():
    # We create a new Page instance, call its AddPage method and store it in a list
    page = Page(content_frame, len(const.pages))
    page.AddPage()
    const.pages.append(page)


# This is where the program begins
if __name__ == "__main__":
     # We create an instance of tkinter
    root = Tk()
    
    # Set his status to zoomed
    try:
        root.wm_attributes("-zoomed", True)
    except TclError:
        root.state('zoomed')

     # Set his title
    root.title("PowerPoint Generator")
    
    # We create a canvas on all the tkinter instance
    canvas = Canvas(root)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # We create a scroll bar on the right side of the screen and take all the height of the page
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    
    # We synchronize the scrollbar and the vue height of the canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # We create a instance of Frame (who gonna contain all the element of the application)
    content_frame = Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # We create another Frame instance to align 2 buttons on the same line
    button_frame = Frame(content_frame)
    button_frame.pack(fill='x', padx=10, pady=10)

    # We create 2 buttons (one right align and the other one left align)
    Button(button_frame, text="Add a new page", command=CreatePage).pack(side='left')
    Button(button_frame, text="Generate ppt file", command=GenerateJSON).pack(side='right')

    # We bind the scrollbar size to the quantity of element contain inside the content_frame
    content_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    content_frame.bind('<Configure>', lambda e: Visualizer(visualizer_frame=const.visualizer_frame, pages=const.pages), add='+')


    root.update()

    visualizer_canvas = Canvas(root, width=root.winfo_screenwidth() - canvas.winfo_width())
    visualizer_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # We create a scroll bar on the right side of the screen and take all the height of the page
    visualizer_scrollbar = Scrollbar(root, orient=VERTICAL, command=visualizer_canvas.yview)
    visualizer_scrollbar.pack(side=RIGHT, fill=Y)

    visualizer_canvas.configure(yscrollcommand=visualizer_scrollbar.set)

    const.visualizer_frame = Frame(visualizer_canvas)
    visualizer_canvas.create_window((0, 0), window=const.visualizer_frame, anchor='nw')
    
    const.visualizer_frame.bind("<Configure>", lambda e: visualizer_canvas.configure(scrollregion=visualizer_canvas.bbox("all")))

    # We start the application
    root.mainloop()