from tkinter import *
from PIL import Image, ImageTk


def SetVisualizerImage(canvas, data):
    if data["Path"] == "":
        return
    
    # Charge l'image avec PIL
    original_image = Image.open(data["Path"])

    # Conversion des dimensions d'origine (cm) en pixels
    # 1 cm = 37.795275591 pixels (approximation courante)
    width_px = data["Width"] * 20 if data["Width"] else original_image.size[0]
    height_px = data["Height"] * 20 if data["Height"] else original_image.size[1]

    # Calcul du ratio d'échelle pour adapter l'image au canvas
    scale_ratio = 0.52916

    # Nouvelle taille redimensionnée
    new_width = int(width_px * scale_ratio)
    new_height = int(height_px * scale_ratio)

    # Redimensionne l'image tout en gardant le ratio d'aspect
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    # Convertit l'image pour l'afficher dans Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)

    # Ajoute l'image au canvas
    canvas.create_image(data["Left"] * 20 * scale_ratio, data["Top"] * 20 * scale_ratio, anchor=NW, image=tk_image)

    # Nécessaire pour garder la référence de l'image dans Tkinter
    canvas.image = tk_image