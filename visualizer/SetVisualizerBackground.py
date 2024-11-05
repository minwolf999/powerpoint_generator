def SetVisualizerBackground(Preview_Canvas, data, width, height):
    r1, g1, b1 = Preview_Canvas.winfo_rgb("#" + data["End"])
    r2, g2, b2 = Preview_Canvas.winfo_rgb("#" + data["Start"])

    # Normalize the RGB values to the range 0-255
    r1, g1, b1 = r1 // 256, g1 // 256, b1 // 256
    r2, g2, b2 = r2 // 256, g2 // 256, b2 // 256

    for i in range(height):
        # Interpolate RGB values for the current step
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)

        # Create the color hex code
        color = f'#{r:02x}{g:02x}{b:02x}'

        # Draw a rectangle that spans the width of the canvas and is 1 pixel tall
        Preview_Canvas.create_line(0, i, width, i, fill=color)