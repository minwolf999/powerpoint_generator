# This function will generate a dict from the datas stores in the list
def GetDatas(pages):
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
                    "Height": child.height,
                }
    
    return data