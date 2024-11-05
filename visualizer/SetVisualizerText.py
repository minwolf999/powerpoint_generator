from tkinter.font import Font


def cm_to_pixels(cm):
    return cm * 37.795275591

def pt_to_pixels(pt):
    return pt * 1.33

def wrap_text(text, font, max_width, canvas):
    lines = []
    current_line = ""

    if max_width == 0:
        max_width = 1
    
    for word in text.split():
        temp_line = canvas.create_text(0, 0, text=current_line+word, font=font)
        line_width = canvas.bbox(temp_line)[2]
        canvas.delete(temp_line)
        
        # Check if the current word is longer than the max_width
        while line_width > max_width:
            # If the current line can accommodate more words
            if len(current_line) + len(word) <= max_width:
                current_line += word + " "
                break
            else:
                # Split the word if it's too long
                if current_line:
                    lines.append(current_line.strip())
                current_line = word[:max_width] + ""  # Split the word
                word = word[max_width:]  # Continue with the remainder of the word
            
            temp_line = canvas.create_text(0, 0, text=current_line+word, font=font)
            line_width = canvas.bbox(temp_line)[2]
            canvas.delete(temp_line)
        else:
            temp_line = canvas.create_text(0, 0, text=current_line+word, font=font)
            line_width = canvas.bbox(temp_line)[2]
            canvas.delete(temp_line)

            # If current line can accommodate the word
            if line_width + 1 <= max_width:
                current_line += word + " "
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "

    # Add the last line if it exists
    if current_line:
        lines.append(current_line.strip())

    return lines


def SetVisualizerText(canvas, data):
    # Convert Left, Top, Width from cm to pixels    
    left_px = int(cm_to_pixels(data["Left"]) * 0.52916)
    top_px = int(cm_to_pixels(data["Top"]) * 0.52916)
    width_px = int(cm_to_pixels(data["Width"]) * 0.52916)

    # Convert FontSize from points to pixels
    font_size_px = pt_to_pixels(data["FontSize"]) * 0.52916

    # Create a custom font with the scaled font size
    font = Font(
        family=data["FontName"],
        size=int(font_size_px),
        weight="bold" if data["Bold"] else "normal",
        slant="italic" if data["Italic"] else "roman",
        underline=data["Underline"]
    )

    # Set the text color
    color = f'#{data["FontColor"]}'

    # Wrap text
    wrapped_lines = wrap_text(data["Text"], font, width_px, canvas)

    # Draw each line at the correct vertical position
    for i, line in enumerate(wrapped_lines):
        line_id = canvas.create_text(
            left_px,
            top_px + i * (font_size_px),  # Add vertical space between lines
            text=line,
            font=font,
            fill=color,
            anchor="nw",  # Anchor at the top-left for each line
            width=width_px,  # Enables text wrapping in the specified width
        )
    
    # Center the text if needed
    if data["Align"] == "center":
        for i, line in enumerate(wrapped_lines):
            bbox = canvas.bbox(line_id)
            text_width = bbox[2] - bbox[0]
            offset_x = (width_px - text_width) / 2
            canvas.move(line_id, offset_x, 0)
    
    # Right align the text if needed
    elif data["Align"] == "right":
        for i, line in enumerate(wrapped_lines):
            bbox = canvas.bbox(line_id)
            text_width = bbox[2] - bbox[0]
            offset_x = width_px - text_width
            canvas.move(line_id, offset_x, 0)