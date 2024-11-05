from tkinter import *

from generateJSON.getDatas import GetDatas
from visualizer.SetVisualizerBackground import SetVisualizerBackground
from visualizer.SetVisualizerText import SetVisualizerText
from visualizer.SetVisualizerImage import SetVisualizerImage

def Visualizer(visualizer_frame, pages):
    if visualizer_frame:
        for widget in visualizer_frame.winfo_children():
            widget.destroy()

    data = GetDatas(pages)

    width = int(25.4*20)
    height = int(19.05*20)

    for i in data:
        Preview_Canvas = Canvas(visualizer_frame, bg='white')
        Preview_Canvas.create_window((0, 0), width=width, height=height)
        Preview_Canvas.pack(anchor='center', side='top')

        for y in data[i]:
            if y == "Background":
                SetVisualizerBackground(Preview_Canvas=Preview_Canvas, data=data[i][y], width=width, height=height)
            if "Path" in data[i][y]:
                SetVisualizerImage(canvas=Preview_Canvas, data=data[i][y])
            if "Text" in data[i][y]:
                SetVisualizerText(canvas=Preview_Canvas, data=data[i][y])