from tkinter import *
import json

from models.pageClass import Page
from PPT_Generation.createPPT import CreatePPT

# This list will store all the pages that will be created 
pages = []

# This function will generate a JSON file with the information entered for the creation of the powerpoint
def GenerateJSON():
    # We initialize the dict that will store the json data
    data = {}

    # We loop on the list
    for page in pages:
        # We initialize the dict of dict
        data[page.name] = {}

        # We set the bacground data for the current page
        data[page.name]["Background"] = {
            "Start": page.start,
            "End": page.end
        }

        # We loop on the elements of each page
        for child in page.children:
            # If the element if a instance of Text
            if type(child).__name__ == "Text":
                # We set the dict of the current text
                data[page.name][child.name] = {
                    "Text": child.text,
                    "Left": child.left,
                    "Top": child.top,
                    "Width": child.width,
                    "Height": child.height,
                    "FontColor": child.fontcolor,
                    "FontSize": child.fontsize,
                    "FontName": child.fontname,
                    "Bold": child.bold,
                    "Italic": child.italic,
                    "Underline": child.underline,
                    "Align": child.align,
                }
            # Or if the element if a instance of Image
            elif type(child).__name__ == "Image":
                # We set the dict of the current image
                data[page.name][child.name] = {
                    "Path": child.path,
                    "Left": child.left,
                    "Top": child.top,
                    "Width": child.width,
                    "height": child.height,
                }
            
    # We create the json file and fill it with the dict store in data
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    # We start the creation of the powerpoint
    CreatePPT("data.json")

    # We stop the application
    root.destroy()


# we create a new page for the future powerpoint
def CreatePage():
    # We create a new Page instance, call its AddPage method and store it in a list
    page = Page(content_frame, len(pages))
    page.AddPage()
    pages.append(page)


# This function handles the mouse scroll event
def on_mouse_wheel(event):
    # event.num is a button of the mouse and event.delta is a scroll unity (start at 0 and can be positive or negative)
    if event.num == 5 or event.delta == -120:
        canvas.yview_scroll(1, "units")
    elif event.num == 4 or event.delta == 120:
        canvas.yview_scroll(-1, "units")
        

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
    scrollbar.pack(side=RIGHT, fill=Y)
    
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

    # We bind the MouseWheel event and 2 button on the mouse to the scroll event
    content_frame.bind_all("<MouseWheel>", on_mouse_wheel)
    content_frame.bind_all("<Button-4>", on_mouse_wheel)
    content_frame.bind_all("<Button-5>", on_mouse_wheel)

    # We start the application
    root.mainloop()