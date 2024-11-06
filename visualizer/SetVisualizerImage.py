from tkinter import *
from PIL import Image, ImageTk

from visualizer.SetVisualizerText import cm_to_pixels


def SetVisualizerImage(canvas, data):
    if data["Path"] == "":
        return
    
    # Charge l'image avec PIL
    original_image = Image.open(data["Path"])

    # Conversion des dimensions d'origine (cm) en pixels
    # 1 cm = 37.795275591 pixels (approximation courante)
    width_px = int(cm_to_pixels(data["Width"]) * 0.52916) if data["Width"] else original_image.size[0] * 0.52916
    height_px = int(cm_to_pixels(data["Width"]) * 0.52916) if data["Height"] else original_image.size[1] * 0.52916


    # Nouvelle taille redimensionnée
    new_width = int(width_px * 0.529)
    new_height = int(height_px * 0.529)

    # Redimensionne l'image tout en gardant le ratio d'aspect
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    # Convertit l'image pour l'afficher dans Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)

    # Ajoute l'image au canvas
    canvas.create_image(cm_to_pixels(data["Left"]) * 0.52916, cm_to_pixels(data["Top"]) * 0.52916, anchor=NW, image=tk_image)

    # Nécessaire pour garder la référence de l'image dans Tkinter
    canvas.image = tk_image